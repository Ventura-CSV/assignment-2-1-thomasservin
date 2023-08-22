def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    number_males = int(input("Enter the number of males:"))
    number_females = int(input("Enter the number of females:"))
    total_students = number_males + number_females 

    m_perc = (number_males / total_students) * 100
    f_perc = (number_females / total_students) * 100

    print(f"Percentage of Males \t {m_perc: .2f}")
    print(f"Percentage of Females: {f_perc: .2f}") 

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
