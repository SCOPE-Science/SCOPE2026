# Exact Lights Out solution counts on Eulerian generalized theta graphs

## Finding
Let \(G(\ell_1,\ldots,\ell_r)\) be the graph consisting of \(r\) internally vertex-disjoint paths, all with the same distinct endpoints \(u,v\), where \(r\ge2\) is even and every path length \(\ell_i\ge2\) is measured in edges. These assumptions make \(G\) a finite, simple, connected Eulerian graph. For \(j\in\{0,1,2\}\), write
\[
t_j=\#\{i:\ell_i\equiv j\pmod3\},\qquad t_0+t_1+t_2=r.
\]
Let \(N_G=I+A_G\) be the closed-neighborhood matrix over \(\mathbb F_2\), and let \(\nu(G)=\dim_{\mathbb F_2}\ker N_G\). Then
\[
\boxed{\nu(G)=\begin{cases}
0,&t_0=0\text{ and }t_1\equiv0\pmod2,\\
2,&t_0=0\text{ and }t_1\equiv1\pmod2,\\
t_0-1,&t_0\ge1\text{ odd},\\
t_0,&t_0\ge2\text{ even}.
\end{cases}}
\]
Starting with every light switched on, the number of distinct solving press subsets is exactly \(2^{\nu(G)}\). In particular, pressing every vertex is the **unique** solution precisely when \(t_0=1\), or when \(t_0=0\) and \(t_1\) is even.

This is a complete classification for the specified graph family, not merely a sufficient criterion. For instance, the four-path graph with lengths \((4,4,5,5)\) has a cycle of length \(9\) but still has a unique all-on solution; the graph with lengths \((3,3,3,3)\) has \(16\) solutions.

## Assumptions and scope
Every path has its own internal vertices, and no edges are included except the edges on those paths. The two terminals are not adjacent because every path has at least two edges. For \(r=2\), the graph is a cycle, including the usual small cycle boundary; the formula is valid. For every even \(r\), all vertices have even degree: the terminals have degree \(r\) and every internal vertex has degree two. Over \(\mathbb F_2\), a press subset \(S\) is represented by its indicator vector \(x\), and it solves the all-on state exactly when \(N_Gx=\mathbf1\). No claim is made here for odd numbers of paths, multigraphs with direct parallel terminal edges, or different toggle rules.

## Proof
We solve the homogeneous system \(N_Gx=0\) completely. Put \(a=x_u\), \(b=x_v\), and \(s_i=x_{i,1}\), the value at the first internal vertex of path \(i\) when oriented from \(u\) to \(v\). At any internal vertex, the homogeneous closed-neighborhood equation is
\[
x_{i,j-1}+x_{i,j}+x_{i,j+1}=0,
\quad\text{hence}\quad
x_{i,j+1}=x_{i,j-1}+x_{i,j}
\quad\text{in }\mathbb F_2.
\]
Thus the values from the first endpoint along a path are periodic with period three:
\[
a,\ s_i,\ a+s_i,\ a,\ s_i,\ a+s_i,\ldots.
\]
The endpoint value at distance \(\ell_i\) must equal \(b\). According to the residue of \(\ell_i\), this forces precisely
\[
\begin{array}{c|c|c}
\ell_i\bmod3&\text{condition}&x_{i,\ell_i-1}\\\hline
0&b=a&a+s_i\\
1&s_i=b&a\\
2&s_i=a+b&s_i
\end{array}.
\]
Here \(s_i\) remains free in the first row, and the listed value in the last column is the internal neighbor of \(v\). These conditions, together with the two terminal equations, are both necessary and sufficient for a null vector, since the internal recurrence reconstructs every remaining coordinate uniquely.

If \(t_0=0\), all first internal values are fixed: \(s_i=b\) on residue-one paths and \(s_i=a+b\) on residue-two paths. The equation at \(u\) is
\[
a+\sum_i s_i=(1+t_2)a+(t_1+t_2)b=(1+t_2)a=0,
\]
where the final equality uses that \(r=t_1+t_2\) is even. The equation at \(v\), because its neighbors contribute \(t_1a+t_2(a+b)\), is
\[
b+t_1a+t_2(a+b)=(1+t_2)b=0.
\]
Since \(t_1\) and \(t_2\) have the same parity, both \(a,b\) are forced to zero when \(t_1\) is even, and both are unconstrained when \(t_1\) is odd. Therefore the nullities are respectively \(0\) and \(2\).

Now suppose \(t_0>0\). At least one residue-zero path forces \(b=a\). On every residue-one path \(s_i=a\), and on every residue-two path \(s_i=a+b=0\). Write \(S\) for the sum in \(\mathbb F_2\) of the \(t_0\) unrestricted first-internal values. The two terminal equations become, respectively,
\[
(1+t_1)a+S=0,\qquad (1+t_0+t_1)a+S=0.
\]
Subtracting them in characteristic two gives \(t_0a=0\). If \(t_0\) is odd, \(a=0\) and \(S=0\), so the \(t_0\) nominally free values satisfy one independent linear equation, leaving nullity \(t_0-1\). If \(t_0\) is even, \(a\) is free and \(S=(1+t_1)a\), which gives \(t_0\) degrees of freedom. This exhausts every case in the formula.

Finally, \(G\) is Eulerian, so every vertex has an even number of neighbors. Consequently
\[
N_G\mathbf1=\mathbf1.
\]
The all-on Lights Out equation \(N_Gx=\mathbf1\) therefore has the particular solution \(x=\mathbf1\) and the complete affine solution set \(\mathbf1+\ker N_G\). It has exactly \(2^{\nu(G)}\) elements. The unique-solution criterion is exactly \(\nu(G)=0\), giving the stated classification. \(\square\)

## Verification
The included standalone Python 3 script `verify.py` constructs the original labelled graphs and forms the actual closed-neighborhood matrix. It compares rank-based nullities against the formula for every ordered length vector in four finite boxes: \(r=2\), lengths \(2\) through \(12\); \(r=4\), lengths \(2\) through \(7\); \(r=6\), lengths \(2\) through \(5\); and \(r=8\), lengths \(2\) through \(4\), totalling \(12{,}074\) graph instances. Additional checks evaluate parity of all matchings by a separate deletion recurrence for \(139\) graphs and enumerate every null press vector for \(41\) small graphs. The script reports `VERIFY_OK 12074` on successful completion. These are finite checks; the proof above, not the finite experiment, supports the universal quantifiers.

## Relationship to prior work
Codsi, Cristancho, Divoux, and Sivashankar (2026) characterize uniquely solvable all-on Lights Out instances by even degree and odd matching parity and give a sufficient condition excluding cycles of length divisible by three (Theorems 2.1 and 4.2). They also note that the absence of these cycles is not necessary. The result here is a concrete, complete, two-terminal family classification that determines the entire kernel dimension and exact number of all-on press solutions, including cases containing cycles divisible by three. It does not claim their general matching-parity criterion, cycle theorem, or all-on linear algebra as new.

A further important earlier source is Dolati and Golalizadeh (2012, Lemma 8), which gives an explicit expression for the **total number of matchings** in generalized-theta graphs. Combined with the determinant/matching-parity criterion of Codsi et al., that earlier formula can in principle decide which graphs have a unique Lights Out solution; uniqueness alone is not asserted to be novel. The point established here beyond such parity information is the **entire nullity in every singular case**, and therefore the exact number of solving press subsets, which matching parity does not determine. The full 2012 article was not accessible during this comparison; this assessment relies on the indexed text of Lemma 8, and differently formulated stronger results remain a risk.

Ballard, Budge, and Stephenson (2014) compute nullities for paths, cycles, and generalized stars assembled by **one-vertex identification**. Their residue-three analysis provides context but does not directly solve the two-terminal compatibility equations for several internally disjoint paths. Batal (2021) gives general edge-addition/removal nullity results rather than the present path-residue classification.

## Limitations
The result applies to simple generalized-theta graphs with an even number of pairwise internally disjoint terminal-to-terminal paths, all of length at least two. It does not address other graph classes or arbitrary modular toggle games. Numerical tests are restricted to the listed finite parameter sets. Literature searches cannot certify historical priority.

## References
1. Julien Codsi, Sergio Cristancho, Alexander Divoux, and Varun Sivashankar, *Extremal Graphs for the Lights Out Problem*, arXiv:2602.07241v1 (first posted 2026-02-06), https://arxiv.org/html/2602.07241v1.
2. Laura E. Ballard, Erica L. Budge, and Darin R. Stephenson, *Lights Out for Related Graphs*, manuscript dated 2014-12-15, https://mgo.syr.edu/wp-content/uploads/2015/10/Lights_Out_Paper.pdf.
3. Ahmet Batal, *Effects of edge addition or removal on the nullity of a graph in the Lights Out game*, arXiv:2108.03059 (2021), https://arxiv.org/abs/2108.03059.
4. Ardeshir Dolati and Somayyeh Golalizadeh, *Sharp bounds for the number of matchings in generalized-theta-graphs*, Discussiones Mathematicae Graph Theory 32(4) (2012), 771–782, DOI:10.7151/dmgt.1646; indexed Lemma 8 via https://bibliotekanauki.pl/articles/743313.pdf (full text access restricted at review).
