# Monitorando logs de app Python com Elasticsearch e Kibana

> Utiliza Docker para executar servidor Elasticsearch e Kibana a fim de monitorar logs de aplicação Python através do Filebeat

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> 
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" /> 
<img src="https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch" />
<img src="https://github.com/cesssar/Elasticsearch_Python/blob/main/Screenshot.png" />

### Estrutura

- Contâiner app Python: salva logs em arquivo JSON
- Contâiner Filebeat: copia os logs e salva no Elasticsearch
- Contâiner Elasticsearch: servidor que processa, armazena e disponibiliza dados em JSON
- Contâiner Kibana: provẽ a interface web com visualizações dos dados salvos no Elasticsearch


### Pré-requisitos

- Docker 


### Elasticsearch

Subir o servidor Elasticsearch

```
docker-compose up -d elasticsearch
```

Se houver falha ao carregar, alterar tamanho máximo de VM (comando para Linux)

```
sudo sysctl -w vm.max_map_count=262144
```


### Gerar token para o Kibana e armazenar ele no .env na chave ELASTICSEARCH_SERVICEACCOUNTTOKEN

Utilizar o login e senha definidos no .env nas chaves ELASTICSEARCH_USERNAME e ELASTIC_PASSWORD logo após o comando -u

```
curl -X POST -u elastic:DkIedPPSCber4563Rweg "localhost:9200/_security/service/elastic/kibana/credential/token/token1?pretty" 
```


### Subir demais serviços

```
docker-compose up -d
```



### Referências

[https://www.elastic.co/guide/en/cloud-enterprise/current/ece-getting-started-search-use-cases-python-logs.html]
[https://www.elastic.co/guide/en/beats/filebeat/8.12/setup-repositories.html#_apt]
[https://akpolatcem.medium.com/building-a-log-pipeline-using-filebeat-elasticsearch-and-kibana-cc853ebb1fbb]
[https://deep-log-inspection.readthedocs.io/en/latest/user/kibana-logs/]
