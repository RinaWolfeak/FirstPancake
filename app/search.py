from flask import current_app

#host = 'localhost'
#port = 9200
#auth = ('admin', 'admin') # For testing only. Don't store credentials in code.
#ca_certs_path = 'C:/Users/wolfe/Downloads/opensearch-2.4.1-windows-x64/opensearch-2.4.1/config/root-ca.pem' # Provide a CA bundle if you use intermediate CAs with your root CA.

#client = OpenSearch(
 #   hosts = [{'host': host, 'port': port}],
  #  http_compress = True, # enables gzip compression for request bodies
   # http_auth = auth,
    # client_cert = client_cert_path,
    # client_key = client_key_path,
    #use_ssl = True,
    #verify_certs = True,
    #ssl_assert_hostname = False,
    #ssl_show_warn = False,
    #ca_certs = ca_certs_path
#)

def add_to_index(index, model):
    if not current_app.OpenSearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.OpenSearch.index(index=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.OpenSearch:
        return
    current_app.OpenSearch.delete(index=index, id=model.id)


def query_index(index, query, page, per_page):
    if not current_app.OpenSearch:
        return [], 0
    search = current_app.OpenSearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']