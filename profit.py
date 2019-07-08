def calculate(distance,no_of_passengers):
    petrol=distance/10
    total_cost=petrol*70
    total_ticket_cost=no_of_passengers*80
    if(total_ticket_cost>total_cost):
      profit=total_ticket_cost-total_cost
      return profit
    else:
        loss=total_ticket_cost-total_cost
        return loss
    #print("total profit=",profit)
distance=30
no_of_passengers=2
print(calculate(distance,no_of_passengers))