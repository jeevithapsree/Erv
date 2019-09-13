image=churn_model_algo
port=8080
version=v7
payload=[{"State":"KS","Account Length":128,"Area Code":415,"Phone":"382-4657","Int'l Plan":"no","VMail Plan":"yes","VMail Message":25,"Day Mins":265.1,"Day Calls":110,"Day Charge":45.07,"Eve Mins":197.4,"Eve Calls":99,"Eve Charge":16.78,"Night Mins":244.7,"Night Calls":91,"Night Charge":11.01,"Intl Mins":10.0,"Intl Calls":3,"Intl Charge":2.7,"CustServ Calls":1}]


build-algo-container:
	docker build  -t $(image):$(version) .

train:
	docker run -v $(CURDIR)/ml:/opt/ml -p $(port):$(port) --rm $(image):$(version) train

serve:
	docker run -v $(CURDIR)/ml:/opt/ml -p $(port):$(port) --rm $(image):$(version) serve

predict: 
	curl --header "Content-Type: application/json" --request POST --data $(payload) http://localhost:$(port)/invocations





