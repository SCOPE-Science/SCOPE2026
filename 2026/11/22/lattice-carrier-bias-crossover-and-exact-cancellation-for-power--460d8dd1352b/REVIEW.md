# Independent mathematical audit

## correctness

PASS

The tail at integer threshold is S(x)=1−[1−(c/x)^p]^κ, x=u+c, and conditioning on Y≥u gives the numerator ∑_{j≥1}S(x+j), not a sum starting at zero. Since S(x) is asymptotic to κc^p x^(−p), finiteness is exactly p>1. The fixed-parameter Taylor remainder is summable uniformly over x+j≥x; upon normalization the remainder through the third survival term is O(x^(1−3p)). Euler–Maclaurin for x^s ζ(s,x+1) gives x/(s−1)−1/2+s/(12x)−s(s+1)(s+2)/(720x³)+O(x^(−5)). The common −1/2 cancels from carrier differences. At p=2, write a=c², d=(κ−1)/2 and e=(κ−1)(κ−2)/6. Then C1=1/6+2da/3 and C3=−1/30−da/6+a²[(2/3)d²−(4/5)e]; the next error is O(x^(−5)). The unique admissible zero of C1 requires a>1/2 and yields C3=(1−4a)/60<0, including −1/20 at a=1. The lattice/carrier ordering off p=2 and the exact κ=1 baseline follow by order comparison, and structural zero inflation cancels at positive thresholds.

## originality

PASS

The supported distinction is the combined sharp population conditional-mean classification for the discretized power carrier, including the admissible cancellation curve and surviving negative cubic term. The count family, continuous parent, mean-excess diagnostic, and classical half-unit correction are not new.

## value

PASS

A mean-excess plot for a tail model depends on the direction and size of the systematic population bias. The result delineates whether discretization or the carrier controls that bias, and resolves the sign and exact changed order on their cancellation boundary. That boundary information is useful even without a uniform or sampling-theoretic extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
