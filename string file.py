#def ravi_kiran(numlist):
 #   even_number=[]

  #  for number in numlist:
   #     if number%2==0:
    #        even_number.append(number)
     #   else:
      #      pass
    #return even_number

#result=ravi_kiran([8,3,4,6])
#print(result)
work_hours=[('abby',100),('kiran',100),('ravi',100)]
def employe_check(work_hours):

    current_salary=0
    employe_month=''
    for employe,hours in work_hours:
        if hours>current_salary:
            current_salary=hours
            employe_month=employe
        else:
            pass
    return(employe_month,current_salary)
rsult=employe_check(work_hours)
print(rsult)