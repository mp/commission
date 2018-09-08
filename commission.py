def main():
  proceed = 'y'

  # Calculate sales commissions
  while proceed == 'y':
    # Get salesperson's sales and commision rate
    sales = float(input('Enter the number of sales: '))
    commission_rate = float(input('Enter the commission rate: '))
    commission = sales * commission_rate
    print('The commission is £', format(commission, ',.2f'), sep='')
    proceed = input('Calculate another commission (type y for yes): ')

main()