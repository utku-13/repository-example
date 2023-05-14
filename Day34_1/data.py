import requests

parameters = {
    "amount":10,
    "type":"boolean"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data = response.json()
question_data = data["results"]
#böyle url içinde de belirtebilirsin ya da paramaters setliyerek de yapabilirsin.
#textler şu an sorunsuz gelsede bazı işaretler olduğu gibi verilmiyor.
# mesela ' işareti &#039 diye geliyor bunları setlemen lazım.




