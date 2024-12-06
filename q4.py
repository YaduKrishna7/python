employees={'Antony':55000,'Susan':45000,'Kiran':60000}
salary_categories=list(map(lambda item:(item[0],'high' if item[1]>=50000 else 'low'),employees.items()))
categorized_employees=dict(salary_categories)
print(categorized_employees)