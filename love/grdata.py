from goodreads import client
import sys

apikey= sys.argv[1]
apisecret= sys.argv[2]

print apikey
print apisecret
client= client.GoodreadsClient(apikey, apisecret)


