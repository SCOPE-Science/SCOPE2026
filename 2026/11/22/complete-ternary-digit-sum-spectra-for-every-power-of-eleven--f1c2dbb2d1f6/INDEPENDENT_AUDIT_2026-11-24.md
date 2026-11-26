# Independent mathematical audit

## correctness

PASS

Writing a ternary weight as a number of power summands and separating exponent representatives modulo the order proves equality with ordered subgroup zero-sum lengths without introducing carries. Modulo 11 there is no negative pair in the odd-order subgroup, and lengths 3, 4, 5 generate all weights at least 3. The order remains five modulo 121; independent bounded generating-function and ordered reachability checks in /workspace/branches/reproduce_3.py recover the 121 multiset counts for t=1..13 as 0,0,0,0,1,0,5,0,10,1,15,5,25. The displayed witnesses agree, and length five extends the block 9..13 to every t>=9. For n divisible by five, v_11(3^n-1)=2+v_11(n/5), by LTE; all exponents yielding 1 must be divisible by five already modulo 11. Thus for k>=2 the subgroup is the entire inverse image of H_2. After freely lifting the first t-1 residues, the negative of their sum reduces to the last unit residue in H_2, so it is automatically an allowed last lift. Reduction proves the converse for every t. The finite checks prove the base census, not the universal lifting. I inspected but did not execute verify.py.

## originality

PASS

The substantive distinct result is the complete stabilized spectrum, particularly the short interior holes 6 and 8 and the first even admissible weight 10, not the previously known minimum or general cofiniteness. The searched power-sum and digital-weight records did not supply that base-level census.

## value

PASS

The failure of the order to grow at the square selects the modulus before enumeration. The exact threshold by parity distinguishes interior obstructions from the known minimum, providing a precise benchmark on sparse-multiple representations at an exceptional prime power rather than an arbitrary list of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
