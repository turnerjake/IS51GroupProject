"""
PSEUDOCODE

main:
    1: Normal Approximation
    2: Z-Score
    3: Function Dictionary
    4: Exit (exit())

normalApproximation:
    n = input
    p = input

    if p > 1:
        error = p should not be larger than 1
    
    q - 1
    np = n * p
    npq = sqrt(n * p * q)
    print(Normal approximation is N(np, npq))

    continue:
        normalApproximation()
    else:
        main()

zScore:
    x = input
    u = input
    o = input

    if o < 0:
        error = o should not be negative
    
    z = (x-u)/o
    print(z)

    continue:
        zScore()
    else:
        main()

functionDictionary:
    functionDefinitions = {
        1: Normal approximation is ...
        2: Z-score is ...
    }

    main()

main()

END PSEUDOCODE
"""