# Independent mathematical audit

## correctness

PASS

At r=2 and b0=(1-s)(1+2gamma)/(2c), the Jacobian at (2,0) has eigenvalues -1,+1. Put v=y,w=x-2+cv, L=1-s, D=L/(2(1+2gamma)), a=c(1+D), K=c(L+D) and p=a/K in (1,2) under the stated s range. Exact Taylor through degree two gives W=-w+a wv+c^2(s-D)v^2+O(3), V=v+D wv-K v^2+O(3); composing shows W_2=w-2a wv+O(3), V_2=v-2K v^2+O(3). Independently recomputed symbolic first-return Taylor coefficients, matching those expressions. For a sufficiently narrow |w|<=Mv positive wedge, H_j=W_j/V_j obeys H_(j+1)=(1-2cs V_j)H_j+O(V_j^2), ensuring invariance and H_j->0. Reciprocal V_j gives V_j=(2K j)^-1+O(log j/j^2), hence n y_n->1/K and n(x_n-2)->-c/K. W_(j+1)=(1-2aV_j)W_j+E_j, E_j=O(V_j^3); positive product P_j~j^-p and sum E_j/P_(j+1)=O(sum j^(p-3)) converges for p<2, including odd-time correction O(V_j^2). Initial w0=theta v0 has signed leading theta v0 versus error O(v0^2), yielding both signs of nontrivial amplitude on open subwedges. No global attraction or p=2 endpoint is proved.

## originality

PASS

Niu–Wang introduced the identical biological map and treated strict stability and other bifurcation regions; the current equality r=2 with neutral predator invasion is a new codimension-two boundary analysis under specified parameters. A separately published Ricker predator-free primitive two-cycle result assumes r>2 and concerns transverse invasion, not this flip/neutral inverse-time dynamics. Standard -1,+1 normal-form techniques motivate but do not supply model-specific coefficients and exponent.

## value

PASS

Natural local boundary of a named positive predator-prey system combines two neutral directions, with an inverse-time predator extinction clock and continuously variable noninteger alternating exponent in an open positive wedge; these are meaningful exact dynamical invariants rather than finite-iterate observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
