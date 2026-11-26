# Independent mathematical audit

## correctness

PASS

Fixed points are exactly y=0. For a second return with y≠0, the first coordinate forces x=−1 and the second then forces y=0. Independently formed both integer Sylvester matrices by using b_j=a_{j+1}−a_j and b_j/y=∏_{ℓ<j}a_ℓ for the iterated coordinates. Their determinants reproduce x(x²+x+1)² for the two third-return quotients, and x³(x²+1)^4 for H=1+x(x+y)(1+y) and the second fourth-return quotient; the first fourth-return quotient is (x+1)H. A common finite root forces the specialized determinant to vanish even if degrees drop: the vector of descending powers of the root ending in 1 is in the Sylvester kernel. For period three, x=0 gives first quotient 1, while x²+x+1=0 gives xy≠0. For period four, if x≠−1 then H=0, so x²=−1 (x=0 is excluded by H=1). At x=−1 the second quotient is −y(y²−2y+2); characteristic two gives no nonzero y, and any root x²=−1 in characteristic two is itself −1. Otherwise this branch yields y=1±i, and on x²=−1 with x≠−1, H=0 reduces to y((x−1)y−2)=0, yielding y=−1−x. Direct iteration of the four candidates gives one directed cycle with four distinct points. The product decomposition counts the fixed points of Φ^4 as ∏(q_j+4ε_j), using cyclicity of the odd field multiplicative groups; removing the ∏q_j fixed points and dividing by four counts exactly the four-cycles, with no periods 2 or 3 appearing via products. For F_5×F_5 the number is (9²−25)/4=14. The replay path for the independent integer determinants is python3 /workspace/reviews/evidence/recompute.py (requires SymPy).

## originality

PASS

The supported contribution is necessity and uniqueness of the four-cycle for arbitrary fields, including odd extensions and the exclusion in characteristic two, with the resulting exact short-period census. Period-two exclusion and prime-field four-cycle existence are established prior overlap, not credited as new. A direct product count is elementary once the exact field-factor census is available; no separate originality claim is made for that counting principle. No inspected statement proves the complete field-factor classification. Earlier inaccessible papers remain a specific risk, not negative evidence and not a reason alone for a verdict.

## value

PASS

Short nontrivial cycles are the basic obstruction to graphs made only of fixed-point components. In the first nontrivial period, the field result replaces isolated existence examples with an exhaustive arithmetic condition and exact multiplicity, and determines the finite reduced product census without scanning the entire functional graph. It also cleanly distinguishes the absence of four-cycles from the potentially much harder absence of all cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
