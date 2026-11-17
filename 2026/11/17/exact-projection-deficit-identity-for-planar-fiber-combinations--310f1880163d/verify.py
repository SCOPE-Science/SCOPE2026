from fractions import Fraction

def main():
    theta = Fraction(1, 2)
    area_k1 = Fraction(4, 1)   # [-1,1] x [-1,1]
    area_k2 = Fraction(8, 1)   # [-2,2] x [-1,1]
    area_fiber_sum = Fraction(4, 1)  # base [-1,1], vertical fiber length 2
    weighted_area = theta * area_k1 + (1 - theta) * area_k2
    deficit_from_areas = weighted_area - area_fiber_sum

    # P1=[-1,1] is contained in P2=[-2,2], so only P2\\P1 contributes.
    # Its total length is 2, and the K2 fiber length is 2 throughout.
    projection_deficit = (1 - theta) * Fraction(2 * 2, 1)

    assert area_fiber_sum == 4
    assert weighted_area == 6
    assert deficit_from_areas == 2
    assert projection_deficit == deficit_from_areas
    assert area_fiber_sum < weighted_area
    print("RECTANGLE_COUNTEREXAMPLE_PASS")
    print("area_fiber_sum=4 weighted_area=6 exact_deficit=2")
    print("FIBER_DEFICIT_IDENTITY_EXAMPLE_PASS")

if __name__ == "__main__":
    main()
