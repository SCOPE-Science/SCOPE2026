# Independent mathematical audit

## correctness

PASS

RESULT.md lines 23–91 give a characteristic-free proof. The independent coordinates of a symmetric multiplication are its values on basis multisets, not the coefficients of its diagonal polynomial. The annihilator of the span of the pure tensors is exactly the space of homogeneous degree-m polynomials vanishing at all K-points. For finite K of order q and m≤q, induct on the number of variables: restriction to the last-coordinate hyperplane vanishes identically by induction, so factor off that variable. On the chart where it is 1, the remaining polynomial has degree ≤m−1<q in each variable; repeated root counting and homogeneity force zero. This includes equality m=q, even in small characteristic. The infinite-field identity principle gives the other positive case. From a basis of N evaluation columns, express the multiplication as a sum of pure forms times vectors v_j; their defining linear forms separate points since all pure forms lie in their span. Defining the jth natural-basis power to be the embedded v_j preserves multiplication and places every ambient product in the embedded image, proving ideal closure and the quotient assertion. For m≥q+1, the natural-basis coordinate difference between the two claimed products factors as a^(m−q−1)(a^q b−a b^q)=0, so the identity holds even for arbitrary-dimensional natural-basis algebras. The two distinct basis multisets have assigned outputs e_1 and 0 in the counterexample, which survives zero padding to every n≥2. In dimension one there are no mixed natural-basis products. Independently enumerated the pure-span over F_4 in dimension two using representatives (1,t) and (0,1), checking rank 4,5,5,5 in arities 3–6 and the failure of the explicit output vector to lie in the span at arities 5 and 6. Replay: python3 -B /workspace/reproductions/check.py 5; output /workspace/reproductions/5.log. Only finite corroboration; the frozen scripts were inspected rather than executed.

## originality

PASS

The sharp algebra-embedding classification survives comparison with the binary predecessor, the closest distinct indexed finite-field envelope, and the classical homogeneous-evaluation boundary. Neither the polynomial rank nor the binary theorem is new. The surviving claim is the characteristic-free universal ideal embedding with this exact threshold, together with the obstruction even to a subalgebra embedding.

## value

PASS

This addresses a specifically posed higher-arity extension. The sharp distinction between field size and characteristic is consequential (for example F_4 permits arity four in characteristic two); the uniform constructive bound and the universal identity obstructing even subalgebra embeddings answer different parts of the embedding problem. This is not simply a dimension calculation for a code or an individual algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
