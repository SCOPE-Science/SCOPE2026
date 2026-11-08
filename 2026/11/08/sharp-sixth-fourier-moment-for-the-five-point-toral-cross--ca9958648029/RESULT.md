# Sharp sixth Fourier moment for the five-point toral cross

## Finding

The simplest two-dimensional coordinate cross is the five-character set \(\Lambda=\{(0,0),(1,0),(-1,0),(0,1),(0,-1)\}\). The sharp sixth-power Fourier synthesis inequality for this support has a nontrivial algebraic extremizer:

\[
\int_{\mathbb T^2}|a+bz+cz^{-1}+dw+ew^{-1}|^6\,dm(z,w)
\le \left(\frac{25}{8}+\frac{35\sqrt{105}}{72}\right)
(|a|^2+|b|^2+|c|^2+|d|^2+|e|^2)^3.
\]

The sharp coefficient is approximately \(8.106156622341471\). Define \(h_*=(15-\sqrt{105})/18\). Equality for a nonzero polynomial holds **if and only if** it is, after multiplication by a nonzero scalar and coordinate rotations \(z\mapsto e^{i\theta}z\), \(w\mapsto e^{i\phi}w\), the polynomial

\[
P_*(z,w)=\sqrt{h_*}+\sqrt{\frac{1-h_*}{4}}(z+z^{-1}+w+w^{-1}).
\]

## Assumptions and scope

The group is the full continuous two-torus \(\mathbb T^2\), not a finite cyclic quotient; \(dm\) is Haar probability measure. Coefficients \(a,b,c,d,e\) are arbitrary complex numbers, including zero. Both sides vanish at the zero polynomial. The claim determines the sixth **power** of the sharp \(L^2\)-to-\(L^6\) norm; the operator norm itself is the positive sixth root of the displayed coefficient. Normalized \(L^2\) energy is exactly the sum of the five squared coefficient magnitudes by orthonormality of characters.

## Proof

**1. Phase majorization.** Let \(x_0=|a|\), \(x_1=|b|\), \(x_{-1}=|c|\), \(y_1=|d|\), and \(y_{-1}=|e|\). Fourier orthogonality gives \(\int|P|^6=\sum_{\nu\in\mathbb Z^2}|\widehat{P^3}(\nu)|^2\). Each coefficient of \(P^3\) is a sum of monomials with nonnegative combinatorial multipliers, so its modulus is bounded by the same sum with coefficient magnitudes. Squaring and summing proves that replacing the five coefficients by their nonnegative magnitudes cannot decrease the sixth moment and keeps the \(L^2\) energy unchanged. All remaining maximizations can therefore be taken over nonnegative coefficients.

**2. Exact pair balancing.** Fix any one coordinate pair and write \(P=D(w)+bz+cz^{-1}\) with \(b,c\ge0\) and \(D(w)=a+dw+ew^{-1}\) having nonnegative Fourier coefficients. Write \(s=b^2+c^2\) and \(t=bc\), so \(0\le t\le s/2\). Expanding the cube and taking its squared \(L^2\) norm in \(z\) gives the identity

\[
\begin{aligned}
\int_{\mathbb T}|D+bz+cz^{-1}|^6\,dm(z)
={}&|D|^6+9s|D|^4+9s^2|D|^2+s^3\\
&+(18|D|^2+6s)t^2+(12|D|^2+18s)t\operatorname{Re}(D^2).
\end{aligned}
\]

On integrating in \(w\), both \(\int\operatorname{Re}(D^2)\,dm(w)\) and \(\int|D|^2\operatorname{Re}(D^2)\,dm(w)\) are nonnegative: they are constant Fourier coefficients of \(D^2\) and \(D^3\overline D\), respectively, and all Fourier coefficients of each product are nonnegative sums of nonnegative monomials. The coefficient of \(t^2\) after integration equals \(18\int |D|^2\,dm+6s\), which is strictly positive whenever the polynomial is nonzero and \(s>0\). Thus the integral is strictly increasing in \(t\in[0,s/2]\), and is uniquely maximized at \(b=c=\sqrt{s/2}\) when \(s>0\). Interchanging the two coordinates yields \(d=e\) under the analogous fixed-energy constraint. In particular every nonzero global maximizer with a nonvanishing coordinate-pair energy is balanced within that pair.

**3. Balance between the two axes.** We have reduced to \(Q=A+X(z+z^{-1})+Y(w+w^{-1})\) with \(A,X,Y\ge0\). Exact Fourier convolution of \(Q^3\) gives

\[
\begin{aligned}
\int|Q|^6={}&A^6+30A^4(X^2+Y^2)+90A^2(X^4+Y^4)
+360A^2X^2Y^2\\
&+20(X^6+Y^6)+180(X^4Y^2+X^2Y^4).
\end{aligned}
\]

With \(r=X^2+Y^2\) and \(q=X^2Y^2\), this expression equals

\[
A^6+30A^4r+90A^2r^2+20r^3+(180A^2+120r)q.
\]

For \(r>0\), the coefficient of \(q\) is strictly positive. Since \(q\le r^2/4\), with equality only for \(X=Y\), balancing the two axes strictly increases the moment unless they already have equal squared magnitudes. This argument also covers the boundary cases \(X=0\) or \(Y=0\).

**4. Unique energy split.** Let \(S=A^2+2X^2+2Y^2>0\). Homogeneity permits \(S=1\); with the proved balances write \(h=A^2\), \(X^2=Y^2=(1-h)/4\), where \(0\le h\le1\). The polynomial in step 3 reduces exactly to

\[
E(h)=\frac{(3h-5)(18h^2-15h-5)}4,
\qquad E'(h)=\frac32(27h^2-45h+10).
\]

The derivative has precisely one root in \((0,1)\), namely \(h_*=(15-\sqrt{105})/18\); it is positive before this root and negative after it, so \(h_*\) is the unique global maximizer on \([0,1]\). Substitution gives \(E(h_*)=25/8+35\sqrt{105}/72\). Because \(0<h_*<1\), all five magnitudes at equality are strictly positive, and the preceding balancing steps force their claimed unique ratios.

**5. Equality phases.** For positive magnitudes, equality in the step-1 triangle inequality for the Fourier coefficient of \(P^3\) at frequency \((1,0)\) compares the terms \(ba^2\) and \(b^2c\); therefore \(\arg b+\arg c\equiv 2\arg a\pmod{2\pi}\). The same argument at \((0,1)\) gives \(\arg d+\arg e\equiv2\arg a\pmod{2\pi}\). These two relations are precisely the statement that, after extracting the global phase \(\arg a\), the phases are additive characters of the exponent lattice on the cross, hence arise from independent torus rotations. Conversely, such rotations and global phase multiplication preserve the sixth moment and the energy. This proves the complete equality classification.

## Verification

A self-contained standard-library Python checker, `checker.py`, computes the exact sixth-moment polynomial by cubing the five-character Fourier series and collecting integer convolution coefficients. It verifies the ten displayed monomial coefficients, the one-variable cubic at four rational points (sufficient for equality of two cubics), and the algebraic critical point numerically as a non-proof consistency check. Run `python3 checker.py`; the recorded output begins `FIVE_MODE_TORUS_L6_PASS moment_monomials=10 rational_tests=4 maximizer=unique`. The quantified theorem and equality classification follow from the analytical proof, not from finite tests.

## Relationship to prior work

Sharp restriction and extension inequalities are sensitive to additive relations among frequency sets. Ciccone and Gonçalves (arXiv:2208.09441, first public 2022-08-19) study sharp continuous Euclidean-circle extension \(L^2(S^1)\to L^6(\mathbb R^2)\) under arithmetic support conditions; their operator and measure are different from five-character synthesis on \(\mathbb T^2\). Germain and Rydin Myerson study spectral projector bounds for broad toral frequency regions; those estimates do not specify the sharp algebraic sixth moment and full optimizers for this exact five-character cross. This theorem is a structured finite-frequency exact case, not a claim of replacing either broader line of analysis. The classical phase-majorant and Fourier-convolution identities are used as established tools.

## Limitations

This is a theorem only for the exact five-frequency cross and normalized Haar measure on the continuous two-torus. It does not give the sharp constant for larger frequency shells, weighted measures, arbitrary finite groups, or any exponent other than six. A broad prior-art search cannot establish absolute historical priority; a previously unlocated exact five-mode computation is a residual possibility. The checker is finite symbolic corroboration and not an independent mathematical audit.

## References

- A. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441 (2022), https://arxiv.org/abs/2208.09441 and https://ar5iv.labs.arxiv.org/html/2208.09441.
- P. Germain and S. L. Rydin Myerson, *Bounds for spectral projectors on tori*, Forum of Mathematics, Sigma (2022), DOI:10.1017/fms.2022.18; full text https://wrap.warwick.ac.uk/id/eprint/165457/1/WRAP-Bounds-for-spectral-projectors-on-tori-Rydin-Myerson-2022.pdf.
