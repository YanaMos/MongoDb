# Docker MongoDB

```

mongodb:
4 shards with 2 replicas (ports 271XX)
3 configuration servers (ports 272XX)
3 entry points to the shard (ports 273XX)

Run
docker-compose -f docker-compose.1.yml -f docker-compose.2.yml  -f docker-compose.cnf.yml -f docker-compose.shard.yml up


```