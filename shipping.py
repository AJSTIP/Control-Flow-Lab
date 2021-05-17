def ground_shipping(weight):

    if weight <= 2:

        return weight * 1.50 + 20.00

    elif weight <= 6:

        return weight * 3.00 + 20.00

    elif weight <= 10:

        return weight * 4.00 + 20.00

    else:

        return weight ** 4.75 + 20.00


print(ground_shipping(8.4))

premium_ground_shipping = 125.00


def drone_shipping(weight):

    if weight <= 2:

        return weight * 4.50 + 0.00

    elif weight <= 6:

        return weight * 9.00 + 0.00

    elif weight <= 10:

        return weight * 12.00 + 0.00

    else:

        return weight ** 14.25 + 0.00


print(drone_shipping(1.5))


def cheapest_method(weight):

    if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:

        return ground_shipping(weight)

    elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:

        return drone_shipping(weight)

    else:

        return premium_ground_shipping


print(cheapest_method(17))
