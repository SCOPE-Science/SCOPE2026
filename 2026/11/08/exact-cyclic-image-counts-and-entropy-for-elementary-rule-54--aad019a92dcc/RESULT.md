# Exact cyclic image counts and entropy for elementary Rule 54

## Finding

Let \(F_n:\{0,1\}^n\longrightarrow\{0,1\}^n\) be elementary cellular automaton Rule 54 on an **indexed cyclic ring**, with indices modulo \(n\), defined by
\[
F_n(x)_i=x_i\mathbin{\oplus}(x_{i-1}\lor x_{i+1}).
\]
Write \(a_n=|\operatorname{im}F_n|\) for the number of **distinct attainable one-step outputs**. For every integer \(n\ge1\),
\[
\boxed{\sum_{n\ge1}a_nz^n=
\frac{z+2z^3+5z^4-4z^5+5z^6+z^7}
{(1+z^2)(1-2z+z^3-z^4)}.}
\]
The first eighteen values are
\[
(a_1,\ldots,a_{18})=(1,2,5,14,22,41,79,150,275,512,959,1793,3343,6239,11650,21750,40598,75785).
\]
Equivalently, for \(n\ge2\), if \(R\) denotes the four complex roots counted with multiplicity of \(t^4-2t^3+t-1\), then
\[
\boxed{a_n=\sum_{r\in R}r^n+2\cos(\pi n/2),\qquad a_1=1.}
\]
The dominant root is
\[
\lambda=\frac{1+\sqrt{3+2\sqrt5}}2=1.866760399\ldots.
\]
Consequently \(a_n=\lambda^n+O(1)\), the attainable fraction is asymptotic to \((\lambda/2)^n\), and the exact one-step output growth rate in bits per site is \(\log_2\lambda=0.900536767\ldots\). Exactly \(2^n-a_n\) indexed length-\(n\) configurations have no predecessor **on a ring of that same length**.

## Assumptions and scope

There is one synchronous update; each of the \(n\) positions is labeled. Output words differing only by rotation are **not** identified. Repeated neighbor indices at \(n=1,2\) are interpreted modulo \(n\), without exclusions. This is the usual Wolfram Rule 54, whose local outputs are one for triples \(001,010,100,101\) and zero for \(000,011,110,111\). No bound is imposed on the number of predecessors of an attainable output.

## Proof

Represent the preceding pair of input bits \((a,b)\) by one of four states \(00,01,10,11\), indexed by \(0,1,2,3\). A local triple \((a,b,c)\) gives an edge \((a,b)\to(b,c)\) labeled by its Rule-54 output. Let \(B_0,B_1\) be the corresponding Boolean adjacency relations, stored as four bit masks (bit \(j\) of row \(i\) means that \(i\to j\) is allowed):
\[
B_0=(1,8,0,12),\qquad B_1=(2,4,3,0).
\]
For an output \(y=(y_0,\ldots,y_{n-1})\), form its **Boolean**, not integer, relation product \(P(y)=B_{y_0}\cdots B_{y_{n-1}}\). A closed length-\(n\) path in this labeled de Bruijn graph is exactly a cyclic length-\(n\) input configuration yielding \(y\). Therefore \(y\in\operatorname{im}F_n\) if and only if at least one diagonal entry of \(P(y)\) is one. This equivalence also holds for \(n=1\) and \(n=2\).

Start with the four-state identity relation and close under right multiplication by \(B_0,B_1\). An exhaustive breadth-first construction produces exactly **109 distinct reachable Boolean relations** (with 77 having a nonzero diagonal). Let \(T\) be the \(109\)-by-\(109\) matrix whose entry \(T_{rs}\) is the number, zero, one or two, of output letters carrying relation \(r\) to relation \(s\). Let \(f\in\{0,1\}^{109}\) record whether each relation has a nonzero diagonal; let \(e\) select the identity relation. Then
\[
a_n=e^{\mathsf T}T^nf\quad(n\ge1).
\]
All integers are exact. Exhaustive closure and matrix-vector arithmetic give the following **componentwise 109-coordinate identity**:
\[
\boxed{T^8f-2T^7f+T^6f-T^5f-T^4f+T^3f-T^2f=0.}
\]
It is checked directly by `verify_relation.py`, which constructs the relations rather than loading a presumed transition table. Multiplication by further powers of \(T\) makes the identity valid in every subsequent degree, so for every \(n\ge8\),
\[
a_n=2a_{n-1}-a_{n-2}+a_{n-3}+a_{n-4}-a_{n-5}+a_{n-6}.
\]
Using \(a_0=1\) as a formal empty-output count and the exact initial values \((a_1,\ldots,a_7)=(1,2,5,14,22,41,79)\) yields the displayed generating function after removing the constant coefficient. This proves the formula for **every** positive length, not only lengths tested by enumeration.

The polynomial \(t^4-2t^3+t-1\) has the factorization
\[
\left(t^2-t-\frac{1+\sqrt5}{2}\right)
\left(t^2-t+\frac{\sqrt5-1}{2}\right).
\]
Its four roots are the stated positive \(\lambda\), a negative real root of magnitude less than one, and a complex-conjugate pair of magnitude less than one. The remaining characteristic factors for the recurrence are \(t^2+1\). The root-power expression satisfies the recurrence and agrees with the exact values for \(2\le n\le7\); the first length is the stated exception. It follows that \(a_n=\lambda^n+O(1)\) with dominant coefficient exactly one. The bit rate and unattainable count follow immediately.

## Verification

From a directory containing the two standalone verifier files, run

```text
python3 verify_relation.py
python3 verify_direct.py
```

`verify_relation.py` independently generates both local transition relations, enumerates all 109 reachable Boolean products, confirms closure and the 109-coordinate identity, and checks the numerator of the rational generating function exactly. `verify_direct.py` instead evaluates \(F_n\) with bit rotations for **every** input on every ring length \(1\le n\le18\), comparing observed distinct outputs to the recurrence. Both programs use only the Python standard library and report success with assertions enabled.

## Relationship to prior work

Martínez, Adamatzky and McIntosh (2014, arXiv:1410.3096v1) present the Rule-54 de Bruijn and subset diagrams and discuss Garden-of-Eden configurations, particularly in Section 3.4. This supplies a natural motivation and a related finite-state language method but does not state the all-length **same-ring cyclic image cardinalities** or the displayed rational generating function. In particular, recognizing a possible bi-infinite output need not ensure a predecessor of the output's **own** period. A count of outputs with exactly one predecessor also does not determine the number with at least one predecessor, as the latter includes all larger fibers. The present formula addresses the latter exact invariant.

## Limitations

The result applies to ordinary Rule 54, exactly one update and equal-length cyclic input/output configurations with labeled positions. It is not a count of all periodic points of the bi-infinite image shift, a multistep image formula, a result for Rule 54's reversible variants, or a classification of predecessor-fiber sizes. The finite relation identity is a reproducible exact computation; independent mathematical verification and exhaustive historical-priority assessment remain to be carried out.

## References

- G. J. Martínez, A. Adamatzky and H. V. McIntosh, *Complete Characterization of Structure of Rule 54*, arXiv:1410.3096v1 (first publicly submitted 2014-10-12), especially Sections 2, 3.3, 3.4 and 4. https://arxiv.org/html/1410.3096v1
