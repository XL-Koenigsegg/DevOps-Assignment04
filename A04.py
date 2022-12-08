def camber(weight,Fcam, Rcam, Froll, Rroll, Fbump, Rbump):
    Frontweight = weight
    Rearweight = 100 - Frontweight

    if Frontweight > 50 & Frontweight == 50:
        print("Front Camber = -0.7\n")
        print("Rear Camber = -0.6\n")
    else:
        print("Front Camber = -0.6\n")
        print("Rear Camber = -0.7\n")

    Fanti = (Frontweight / 100) * 64
    Ranti = (Rearweight / 100) * 64

    print("Front anti-rollbar: " + str(Fanti))
    print("Rear anti-rollbar: " + str(Ranti))

    Frebound = 19 * (Frontweight / 100) + 1
    Rrebound = 19 * (Rearweight / 100) + 1

    print("Front Rebound: " + str(Frebound))
    print("Rear Rebound: " + str(Rrebound))

    Fbump = Frebound * 0.6
    Rbump = Rrebound * 0.6

    print("Front Bump: " + str(Fbump))
    print("Rear Bump: " + str(Rbump))


WeightDis = int(input("Enter weight distribution: "))
FrontCamber = int(input("Front camber: "))
RearCammber = int(input("Rear camber: "))
FrontRoll = int(input("Front anti-rollbar: "))
RearRoll = int(input("Rear anti-rollbar: "))
FrontBump = int(input("Front bummp stiffness: "))
RearBump = int(input("Rear bump stiffness: "))

camber(WeightDis, FrontCamber, RearCammber, FrontRoll, RearRoll, FrontBump, RearBump)