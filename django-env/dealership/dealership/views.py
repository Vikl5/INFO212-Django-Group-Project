from urllib import response
from .models import Car, Customer, Employee
from rest_framework.response import Response
from .serializers import CarSerializer, CustomerSerializer, EmployeeSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

#Following code is taken from the Lecture notes in INFO212
#LECTURE 08: ARCHITECTURAL SOLUTIONS - Fazle  Rabbi 2022
#https://mitt.uib.no/courses/35975/files?preview=4543975

@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#############################################################
#Customers

@api_view(['GET'])
def get_customers(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCustomer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#############################################################
#Employees

@api_view(['GET'])
def get_employee(request):
    customer = Employee.objects.all()
    serializer = EmployeeSerializer(customer, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theEmployee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theEmployee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

###########################################################
#Our own code, but still uses some of the same methods as provided in the lecture
#Order-car

@api_view(['GET'])
def order_car(request, car_id, customer_id):
    try:
        theCustomer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        theCar = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if theCar.status == 'booked':
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif theCar.status == 'available':
        theCar.status = 'booked'
        theCustomer.customer_booking = theCar
        theCar.save()
        theCustomer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def cancel_order_car(request, car_id, customer_id):
    try:
        theCustomer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        theCar = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #if theCustomer.customer_booking == theCar:
    if theCustomer.customer_booking == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif theCar.status == 'booked' or theCar.status == 'rented': #and theCar == theCustomer.customer_booking:
        theCar.status = 'available'
        theCar.save()
        theCustomer.customer_booking = None
        theCustomer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def rent_car(request, car_id, customer_id):
    try:
        theCustomer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        theCar = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if theCustomer.customer_booking == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif theCar.status == 'booked':
        theCar.status = 'rented'
        theCar.save()
        theCustomer.customer_booking = theCar
        theCustomer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def return_car(request, car_id, customer_id):
    car_status = ['available', 'damaged']
    try:
        theCustomer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        theCar = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if theCustomer.customer_booking == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif theCar.status == 'booked' or theCar.status == 'rented':
        theCar.status = random.choice(car_status)
        theCar.save()
        theCustomer.customer_booking = None
        theCustomer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)