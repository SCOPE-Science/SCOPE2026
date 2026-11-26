# Independent mathematical audit

## correctness

PASS

With q⁻² normalized inversion, the complex convolution norm equals the kernel's ℓ¹ norm by choosing conjugate phases at a single output location. Complete-parabola sums have modulus sqrt(q) for b≠0 and are q times the indicator of a=0 on b=0, so the latter slice changes by exactly D_q(B)/q². On b≠0 put u=E conjugate(G)/sqrt(q); summing over all a there, the linear moment is hq(q−1)/sqrt(q) and the sum of (Im u)² is hq(q−h)/2. The latter follows by comparing |E|² with Re(E² conjugate(G)²/q): equal sums and squared sums force equality of unordered pairs in odd characteristic, giving 2h²−h ordered pairings before the b=0 subtraction. The two normalized Taylor terms sum to −3h/(4 sqrt(q))+h(4−h)/(4q^(3/2)). The cubic uses Re(u|u|²−u³)/4: for the first correlation (r−s)(t−s)=0 gives exactly 2h²−h configurations before subtracting b=0; for the other, choose the three erased coordinates and one unrestricted coordinate, then solve a quadratic for at most two remaining ordered pairs. Both normalized cubic contributions are O(h³ q^(−3/2)). Uniform Taylor control for |u|/sqrt(q)≤1/4 gives the O(h⁴ q^(−3/2)) remainder. Uniform fibres of the nontrivial character applied to a(u−v), and the odd-p cosine sum, give the displayed two-erasure coefficient. As an independent geometry check, in F_(3^m) an erased three-point F3-line has total ℓ¹ sum q, whereas {0,x,y} with x,y F3-independent has q(3+6 sqrt(3))/9 by the nine equally frequent phase pairs; subtract 6 in both cases. All checks are replayable from RESULT.md Steps 1–5 and these counts. The bundled checker was inspected, not executed; its samples principally check normalization and moments, not the uniform theorem. The strict leading-decrease interpretation is for fixed h, not all h permitted by the error bound.

## originality

PASS

Credit the known complete Gauss-sum baseline and the standard Fourier-algebra/convolution identity. The distinct result is the normalized averaged perturbation for arbitrary small masks, in particular the universal −3h/(4 sqrt(q)) and exact one-dimensional spectral term at the next fixed-h order. Inspected primary synthesis and indexed erasure/moment results neither state nor imply both terms and their uniform remainder.

## value

PASS

The Fourier-algebra norm measures the sharp endpoint cost for a standard finite-field frequency set. The theorem separates a universal cardinality loss from an arithmetic and geometric correction for arbitrary small masks over prime-power fields. The two-point characteristic dependence and the three-point geometry example show the correction is informative, rather than solely a nonsharp uniform bound. The useful asymptotic interpretation is fixed h; the expression is not a finite-q closed form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
