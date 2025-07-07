## Creating a postgres docker

sudo docker run --name healthcare \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=passwd \
  -e POSTGRES_DB=healthcare \
  -p 5432:5432 \
  -d postgres


## Logging into psql
sudo docker exec -it healthcare psql -U admin -d healthcare


