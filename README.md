# NLSE
In this repository, we provide codes for simulating the nonlinear Schrödinger equations for different optical regimes, considering the focusing (attractive) regime.

The propagation of light in a nonlinear medium is described by a Nonlinear Schrödinger equation (NLSE). Depending on the intensity of the light field amplitude, the system's response, which is given by its susceptibility will have a different functional form.

Here we implement the NLSE for three different regimes: Kerr medium ($\chi^{(3)}$ regime), that is, when the refractive index varies linearly with the intensity; the $\chi^{(3)}+\chi^{(5)}$ regime which is up to second order in the intensity, and finally, the most general saturating nonlinearity.

There are codes for solving the NLSE in one and two dimensions for the above-mentioned regimes, for both imaginary and real time. The former will be used when we are interested in assesing the groundstate of the system, while the latter will be used for studying the real-time dynamics. These codes were used for the numerical simulations of the NLSE's analysed in the work of Ref [1].

All codes have been adapted from templates available on the webpage of the XMDS project[2].

## Instructions
Further instructions regarding compilation, execution and analysis of the data can be found on http://www.xmds.org/.

## Further comments
The codes whose names contain *Hankel transform* are 1D numerical simulations. 

Due to the radial symmetry present in most cases, we can use the Hankel transform to reduce from a 2D to 1D system, in addition, to speeding up the simulations. For most of the simulations in 2D, the codes have been parallelized. For detailed instructions on how to run them, please refer to the documentation on http://www.xmds.org/. 

Finally, the code *townes_soliton_equationSolver.py* written in python is used to solve the cubic NLSE. When waveguide solutions area assumed, we can eliminate the dependence on the time coordinate. Taking advantage of the radial symmetry, we are left with an equation for the radial coordinate only. Its solution above a critical power is the Townes soliton. More details can be found in the work of Ref [1].

## Bibliography
[1] H. da Silva, R. Kaiser et T. Macrì., arXiv:2211.07037 (2022).

[2] G. R. Dennis et al., Comput. Phys. Commun. 184, 201 (2013).

