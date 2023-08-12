def calculate_quantum_numbers(coeff, exponent):
    n = coeff
    ell = n-1
    m_ell = [x for x in range(-ell, ell + 1)]

    k = len(m_ell)
    remainder = exponent % k
    qoutiont = exponent // k
    if qoutiont % 2 == 0:
        m_s = 1/2
    else:
        m_s = -1/2

    return {"n": n, "ell": ell, "m_ell": m_ell, "m_s": m_s}
    
print(calculate_quantum_numbers(2, 5))