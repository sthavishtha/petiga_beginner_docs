.. role:: envvar(literal)
.. _nse:

Tutorial 3: unsteady incompressible Navier-Stokes equations
===========================================================

**Objective:** At the end of this tutorial you will understand how to
use this software framework to solve the unsteady fluid mechanics problem.

We solve the incompressible Navier-Stokes equations stabilized with the variational multiscale method as formulated. Let :math:`\Omega \subset \mathbb{R}^d` be an open set, where :math:`d=2,3`. The boundary of :math:`\Omega` with unit outward normal is denoted :math:`\Gamma`. The problem can be stated in strong form as: find the velocity :math:`u: \Omega \times (0,T) \rightarrow \mathbb{R}^d` and the pressure (divided by the constant density) :math:`p: \Omega \times (0,T) \rightarrow \mathbb{R}` such that,

.. math::
   :nowrap:

   \[
   \begin{align*}
   &\frac{\partial u}{\partial t} + u\cdot(\nabla u) + \nabla p = 1/\mu\Delta f &in  :\Omega\times(0,T),\\
   &\nabla\cdot u = 0 &in :\Omega\times(0,T),
   \end{align*}
   \]

.. math::

   u = 0 \quad \text{on} \quad \Gamma \times (0,T),

.. math::

   u(\cdot, 0) = u_0(\cdot) \quad \text{in} \quad \Omega,

where :math:`u_0` is the initial velocity, :math:`f` represents the body force per unit volume, and :math:`\nu` is the kinematic viscosity. We solve a turbulent flow in a rectangular box the results of which we plot in :ref:`nse_plot`. The domain is periodic in the streamwise direction, which we set using the function :envvar:`IGAAxisSetPeriodic` in the code. No-slip boundary conditions are set at the top and bottom boundaries and the initial condition is set using a laminar flow profile. The simulation is forced using a pressure gradient in the form of a body force in the streamwise direction.

.. _nse_plot:

.. figure:: ./qcriterion_isocont.png
   :alt: Description of the plot
   :align: center
   :figwidth: 60%

   Figure: Turbulent flow in a rectangular box. The plot shows the iso-contours of the Q-criterion.

The command to run after compilation

mpirun ./NavierStokesVMS -options_file params.txt > output.o

.. Local Variables:
.. mode: rst
.. End: