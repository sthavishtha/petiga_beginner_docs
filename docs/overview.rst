.. role:: option(literal)
.. role:: file(literal)
.. _overview:

Overview
========

`PetIGA`_ is a software framework that approximates the solution of partial differential equations using isogeometric analysis. It is an extension of `PETSc`_, adding the NURBS discretization capability and the integration of forms. This framework can be used to solve linear, nonlinear, time-dependent, or time-dependent nonlinear problems. In this framework, the user has to provide the evaluation of the linear form (right-hand side, or residual of a nonlinear problem) at a Gauss point, as well as the bilinear form (left-hand side or Jacobian of the nonlinear residual). The framework is designed so that researchers can focus on the physics of the problem and ignore issues of parallelism and performance.

**Key Features of PetIGA**

- *Integration with PETSc*: It leverages PETSc, a high-performance library, to handle large-scale scientific computations and parallelism.
- *Flexibility and Robustness*: PetIGA supports various nonlinear and linear problems in solid and fluid mechanics, demonstrating strong scaling on up to 4096 cores.
- *Parallel Scalability*: The framework is well-suited for large-scale applications, ensuring efficient parallel scalability.
- *Support for Numerical Differentiation*: PetIGA includes support for numerical differentiation, which is essential for evaluating the Jacobians.
- *Open-Source and Extensible*: The framework is open-source and designed to be reusable, promoting code reuse and flexibility in scientific research.

**Objective of this documentation**

This documentation provides an overview of the PetIGA framework, including its features, capabilities, and applications. It is intended for beginners who want to understand the usage of PetIGA. The documentation covers some simple tutorials and examples to help users get started with the framework and apply it to solve real-world problems in solid and fluid mechanics.

.. _PETSc: https://www.mcs.anl.gov/petsc/
.. _PetIGA: https://github.com/dalcinl/PetIGA

.. Local Variables:
.. mode: rst
.. End:
