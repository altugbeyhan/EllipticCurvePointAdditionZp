def EllipticCurvePointAddition(a,b,p,P,Q):
    # P=(x1,y1), Q = (x2,y2)
    try:
        if P != Q:
            m = ((Q[1]-P[1])*pow((Q[0]-P[0]),-1,p)) % p
        else:
            m = (((3*(P[0])**2)+a)*pow((2*P[1]),-1,p)) % p
        print(f"P+Q=({((m**2)-P[0]-Q[0]) % p},{(m*((P[0]-((m**2)-P[0]-Q[0])))-P[1]) % p})")
    except:
        print("P+Q=Inf")

EllipticCurvePointAddition(a=0, b=3, p=7, P=(2,2), Q=(3,4)) # (6,4)
EllipticCurvePointAddition(a=0, b=3, p=7, P=(2,2), Q=(2,2)) # (5,3)
EllipticCurvePointAddition(a=0, b=3, p=7, P=(2,2), Q=(2,5)) # Inf
