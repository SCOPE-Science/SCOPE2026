# Independent mathematical audit

## correctness

PASS

For the displayed P_n over C, differentiation gives (wx,wy,wG_z,xy+R) with R=G+wG_w=(n+2)G/2-zG_z/2. In B[x,y]/(xy+R) the monic reduction xy=-R leaves the B-basis 1,x^i,y^j (i,j>0); the scalar coefficient of any multiple of wx, wy, or wG_z is in (wR,wG_z), and both these scalar generators belong to that ideal. Cancelling w in B therefore gives exactly (G,G_z) as the kernel of b -> bw, with x and y killing the image. For g=G(z,1), the coefficient of z^(n-2k) in the asserted ODE is -4k(k+1)c_k + alpha(n-2k+2)(n-2k+1)c_(k-1), with alpha=8/[n(n-1)] and the second term absent at k=0; the supplied coefficient ratio makes this zero. At a repeated root away from ±sqrt(alpha), the g'' term has a nonzero term of strictly lower vanishing order than the others, a contradiction. At the two exceptional points, positivity and parity rule out any zero. Scaling z by a square root of nonzero w and checking w=0 shows the common zero set of G,G_z is just the origin. Thus they are a regular sequence. The shifted Koszul resolution is minimal, gives the stated Hilbert series and length n(n-1)/2, and places the top module degree at 2n-2. This proves (w)^n=0 while quotienting by w gives the reduced hypersurface xy+z^n=0, so (w) is the entire nilradical without any further radical assumption. Reducing the module modulo w gives exactly its first layer, and additivity gives the full ring series (with half-integral x,y weights if n is odd). Independent ancillary check: `python /workspace/replay/nilradical.py` computes exact homogeneous relation ranks for n=4..10; lengths 6,10,15,21,28,36,45, with the predicted graded dimensions. The analytic/algebraic proof, not this finite check, covers every n>=4.

## originality

PASS

Credit Kang for the potential, the reduced locus, the generator w and the nilradical-filtration question. The supported distinct contribution is the exact annihilator and uniform finite weighted complete-intersection calculation for the entire ideal (w); the graded module invariants follow from that calculation. The first layer alone can be read off from the derivative presentation modulo w² and is not treated as independently substantive novelty.

## value

PASS

The reduced Kleinian surface loses precisely the scheme structure studied here. Identifying all nilpotents as a finite graded module with an exact annihilator and length supplies usable local data for every parameter in a family singled out by a prior syzygy construction. This advances the stated filtration question without purporting to solve all higher layers. The value is the uniform scheme-theoretic calculation, not the numerical spot checks or the formal Hilbert-series manipulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
