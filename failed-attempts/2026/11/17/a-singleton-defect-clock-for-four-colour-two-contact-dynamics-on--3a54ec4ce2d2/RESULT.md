# A singleton-defect clock for four-colour two-contact dynamics on complete graphs

## Finding
Let \(F_n\) be the synchronous four-colour cyclic successor-contact automaton with contact threshold two on the simple complete graph \(K_n\), with \(n\ge2\) labelled vertices. For an initial configuration \(x\), let \(\tau(x)\) be its least nonnegative first-periodic-entry time, and let \(p(x)\) be its eventual least temporal period. Then the only possible pairs \((\tau,p)\) are \((0,1),(1,1),(2,1),(3,1),(0,4)\). Define
\[
H(z)=e^z-1-z.
\]
The exact number \(A_{t,p}(n)\) of labelled initial configurations with \((\tau,p)=(t,p)\) is \(n![z^n]Q_{t,p}(z)\), where
\[
\begin{aligned}
Q_{0,1}(z)&=(1+z)^4+4H(z)(1+z)^2+2H(z)^2,\\
Q_{1,1}(z)&=4H(z)z(1+z)^2+2H(z)^2(z^2+4z+2),\\
Q_{2,1}(z)&=4H(z)^2\bigl(H(z)+z+z^2\bigr),\\
Q_{3,1}(z)&=4zH(z)^3,\\
Q_{0,4}(z)&=H(z)^4.
\end{aligned}
\]
In particular, \(F_n^7=F_n^3\) on every initial configuration. The sharp maximum first-periodic-entry time is
\[
\max_x\tau(x)=\min\left(3,\left\lfloor\frac{n-1}{2}\right\rfloor\right).
\]
Primitive four-cycles occur precisely when \(n\ge8\), and their orbit count is \(n![z^n]H(z)^4/4\). The sharp three-step class occurs precisely when one colour is occupied once and each of the other three colours at least twice; consequently it first exists at \(n=7\) and has population \(4n![z^n]zH(z)^3\).

Conditioned on *not* being initially periodic, uniformly random labelled four-colour configurations exhibit the limiting singleton-defect law
\[
\Pr\{\tau=3\mid\tau>0\}
=\frac{n}{n+3}+O\!\left(n^2(2/3)^n\right),
\qquad n\to\infty.
\]
For this model, configurations that are initially periodic are exactly those fixed immediately or having primitive period four; thus the condition \(\tau>0\) is equivalent to *not initially periodic*. The implied constant in the error is absolute.

## Assumptions and scope
The graph \(K_n\) is loopless; each vertex has one colour in \(\mathbb Z/4\mathbb Z\). At each integer time, a vertex of colour \(c\) changes to \(c+1\bmod4\) if at least two *distinct* vertices currently have colour \(c+1\bmod4\), and otherwise retains \(c\). Every vertex updates simultaneously, and labels are fixed. All formulas hold for each integer \(n\ge2\). The count of a temporal orbit is distinct from the count of starting configurations: divide the primitive-four population by four to count its orbits.

## Proof
For any state, let \(m_i\) be the number of vertices of colour \(i\) and interpret indices cyclically modulo four. The colour-class counts evolve by the exact identity
\[
m_i'=m_i\mathbf 1_{m_{i+1}<2}+m_{i-1}\mathbf 1_{m_i\ge2}.
\]
This works because every vertex of colour \(i\) sees all vertices of its successor colour as neighbours, whereas it never sees itself as a successor-colour neighbour. It follows that the three-category signature \(s_i\in\{0,1,H\}\), recording whether \(m_i=0\), \(m_i=1\), or \(m_i\ge2\), evolves autonomously. With predecessor \(a=s_{i-1}\), current symbol \(b=s_i\), and successor \(c=s_{i+1}\), the next signature symbol is
\[
\phi(a,b,c)=
\begin{cases}
0,&b=0,\\
0,&b=1,\ c=H,\\
1,&b=1,\ c\ne H,\\
H,&b=H,\ c\ne H,\\
a,&b=H,\ c=H.
\end{cases}
\]
For any signature other than \((H,H,H,H)\), the following complete case split shows that its colour groups stop moving in at most three steps. The cases are organized by the number of heavy symbols.

If there are no heavy symbols, all vertices are fixed. With one heavy symbol, the state is already fixed unless its immediately preceding colour is a singleton, in which case that singleton moves once and the state is fixed. With two opposite heavy symbols, any preceding singleton moves once and the state is then fixed; with two adjacent heavy symbols, the trailing heavy group moves into the following heavy group, and a singleton preceding the pair, if present, takes one further step. With three heavy symbols, the omitted fourth colour is either absent or a singleton, giving exactly two or three steps respectively. With four heavy symbols, every vertex advances once per sweep and the state lies on a primitive four-cycle.

The case distinction is exhaustive: it covers all \(3^4=81\) signatures. For states not having four heavy colours, a fixed signature has no occupied colour immediately preceding a heavy colour, which is precisely the condition for *every vertex* to be fixed. In particular there is no hidden label permutation after the count signature stops. Hence the signature clock equals the true first-periodic-entry clock, and the only nonfixed recurrent sector is the all-heavy sector. The four-heavy case gives primitive period exactly four, since each vertex's colour increments on every update.

Give a missing colour weight \(1\), a singleton colour weight \(z\), and a heavy colour weight \(H(z)=\sum_{j\ge2}z^j/j!\). Multinomial label allocation makes the product of these four weights the exponential generating function of a signature class. The preceding case split yields the five complete class polynomials:
\[
\begin{array}{c|l}
(\tau,p)&\text{weighted sum over signatures}\\\hline
(0,1)&(1+z)^4+4H(1+z)^2+2H^2\\
(1,1)&4Hz(1+z)^2+2H^2(z^2+4z+2)\\
(2,1)&4H^2(z+z^2+H)\\
(3,1)&4zH^3\\
(0,4)&H^4
\end{array}
\]
The five expressions sum exactly to \(e^{4z}\). Existence of the sharp clock at the smallest allowed circumference follows from the minimal vertex populations of signatures \((1,H,H,H)\), \((0,H,H,H)\), \((1,H,H,0)\), and \((1,H,0,0)\), up to rotation; these first supply depths three, two, one, and zero at sizes seven, five, three, and two. The asserted cutoff and the identity \(F_n^7=F_n^3\) follow.

Finally, four-colour occupancy is multinomial under uniform random colouring. The event that a given colour is non-heavy has exact population \(3^n+n3^{n-1}\). Pairwise intersections have population \(O(n^2 2^n)\), hence the population of initially non-period-four states is
\[
4(3^n+n3^{n-1})+O(n^2 2^n).
\]
The fixed-state population is \(n![z^n]Q_{0,1}=O(n^2 2^n)\), so subtracting it from the non-period-four population gives the same leading expansion for the number of states with \(\tau>0\). The three-step population is \(4n![z^n]zH^3=4n3^{n-1}+O(n^3 2^n)\), by excluding from the remaining three classes all occupancies below two. Dividing the latter estimate by the corrected \(\tau>0\) population gives the displayed conditional limit with the stated error.

## Verification
The standalone script `category_certificate.py` exhaustively checks the \(81\) three-symbol signatures, their destinations, the exact weighted polynomial table and the unique depth-three patterns. The distinct script `direct_validation.py` independently iterates the full labelled state space at every ring size \(2\le n\le9\) and compares exact orbit entry and period counts against coefficients obtained by a separate integer-only convolution for the heavy-class exponential generating function. Both scripts use only the Python standard library and are replayable with `python3 category_certificate.py` and `python3 direct_validation.py`; their actual outputs are included as `category_output.txt` and `direct_output.txt`.

## Relationship to prior work
The cyclic successor-contact model and higher contact thresholds are described in Fisch–Gravner–Griffeath (1993). The 2016 Gravner–Lyu–Sivakoff work treats three colours and threshold-one dynamics on arbitrary graphs; those results do not give the present four-colour, two-contact labelled entrance-time polynomial. Bello–Sivakoff (2021), inspected in full at its theorem statements and model setup, studies threshold-at-least-two dynamics on infinite regular trees with probabilistic fixation/fluctuation results, which do not imply finite complete-graph time-class counts. The closest accessible related mathematical records concern complete graphs with three colours, four colours with threshold one, and four-colour contact dynamics on complete bipartite or tripartite graphs. None of those statements, under their stated hypotheses, implies this exact threshold-two complete-graph result.

## Limitations
The result is confined to simultaneous updates on simple complete graphs and the specific parameter pair of four colours and threshold two. It does not classify arbitrary graphs, arbitrary thresholds, or transient attractor-basin sizes separated by the final fixed colouring. The early threshold papers were available only in abstract/bibliographic form for this comparison, and historical priority is not fully settled. All infinite-size conclusions follow from proved finite-population formulas, not finite simulation. Independent validation has not been performed.

## References
1. R. Fisch, J. Gravner, and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, first posted 1993-04-02. https://arxiv.org/abs/patt-sol/9304001
2. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, 2016-10-24. https://arxiv.org/abs/1610.07320
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees*, arXiv:2108.06404, 2021-08-13. https://arxiv.org/abs/2108.06404
