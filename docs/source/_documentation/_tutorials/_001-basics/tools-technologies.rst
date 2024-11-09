.. Author: Akshay Mestry <xa@mes3.dev>
.. Created on: Wednesday, November 06, 2024
.. Last updated on: Friday, November 08, 2024

:og:title: Tools and Technologies
:og:description: Tools to empower your Open Science workflows.

.. _tools-technologies:

===============================================================================
Tools and Technologies
===============================================================================

.. title-hero::
    :icon: fa-brands fa-python
    :summary:
        Equip yourself with the essential tools required for efficient coding,
        data analysis, and collaboration in Open Science.

.. tags:: getting-started, open-science-101

.. contributors::
    :location: Chicago, IL
    :timestamp: November 08, 2024

    - :name: Akshay Mestry
    - :email: xa@mes3.dev
    - :headshot: https://avatars.githubusercontent.com/u/90549089?v=4
    - :github: https://github.com/xames3
    - :linkedin: https://linkedin.com/in/xames3
    - :orcid: https://orcid.org/0009-0000-4562-8983
    - :status: Open Source Maintainer

In the world of :term:`Open Science`, collaboration and innovation go
hand-in-hand. Scientists, researchers, and contributors from across the globe
come together to share data, insights, and breakthroughs. However, this
collaboration requires more than just ideas |html-dash| it requires the right
set of tools. These tools serve as the backbone for everything from coding and
data analysis to version control and publishing. Without them, the journey
from concept to contribution would be slow, error-prone, and often
overwhelming. In this context, tools refer to a collection of software
programs, platforms, and environments that allow you to efficiently work with
code, manage versions, handle data, and even collaborate in real time. Each
tool plays a specific role in the research and development process, addressing
different challenges:

.. tab-set::

    .. tab-item:: VCS

        :term:`Version Control System` like Git and SVN allow you to track
        changes in code, ensuring you never lose work and can collaborate
        seamlessly with others.

    .. tab-item:: IDE

        :term:`Integrated Development Environment (IDE)` like Visual Studio
        Code provide a space to write, debug, and test code with features that
        make your workflow faster and more intuitive.

    .. tab-item:: Data processing tools

        :term:`Data processing tools` like Jupyter Notebook facilitate
        interactive data analysis, letting you run code in chunks, visualize
        outputs, and document results in one place.

    .. tab-item:: Package managers

        :term:`Package managers` like Conda help you manage software libraries
        and environments, ensuring that you're working with the right versions
        of the tools for your project.

These tools are more than just software |html-dash| they are the enablers
of :term:`Open Science`. They streamline workflows, reduce friction, and
help build a shared language across diverse disciplines. By mastering
these tools, you become empowered to focus more on your research and less
on the technical overhead. They allow you to engage in the spirit of Open
Science |html-dash| transparently, collaboratively, and efficiently.

.. _about-git:

-------------------------------------------------------------------------------
Git
-------------------------------------------------------------------------------

Git is a powerful, distributed :term:`version control system` that enables you
to track changes in your code and data over time. Git is not just a tool but
an essential framework that supports open science through efficient, organized
collaboration on data, code, and research. Like mentioned earlier, Git is a
distributed version control system, meaning it allows multiple contributors to
work on a project simultaneously and independently, while maintaining an
organized record of changes.

.. image:: ../../../_assets/guides/git-banner.png
    :alt: Git banner

.. _understanding-git:

Understanding Git
===============================================================================

- **Collaborating on Code for Data Analysis.** Imagine a team of researchers
  working on a data analysis project. Each researcher can create their own
  branch to experiment with different data cleaning methods, machine learning
  models, or visualizations. They can commit their changes, track progress,
  and merge successful ideas into the main branch. This structure encourages
  collaborative testing while ensuring stability.
- **Version Control for Data and Documentation.** Git can be used to version
  not only code but also datasets, notebooks, and documentation. If
  researchers make updates to data preprocessing methods, for example, they
  can use Git to track those changes and ensure that documentation remains
  aligned with the current state of the data.
- **Publishing Open Access Research.** By pushing project repositories to
  platforms like :ref:`about-github` or GitLab, researchers can easily share
  their work with the global community. GitHub repositories can even be linked
  to :ref:`about-zenodo`, allowing for citable versions of the project,
  complete with DOI generation. This setup is ideal for open science, where
  making research outputs available and citable is critical.

Three core concepts
===============================================================================

- **Repositories.** A repository (repo) is essentially a project folder where
  Git tracks changes. Repositories can be local (on your machine) or remote
  (hosted on platforms like GitHub or GitLab). :term:`Open Science` projects
  often have both local and remote repositories.
- **Branches.** A branch is an independent line of development within a
  repository. By default, Git creates a main branch, but contributors can
  create additional branches to work on new features or experiments without
  disturbing the main codebase. Branches are essential in open science
  projects as they allow for experimentation and modularity. For example,
  researchers can create a branch to test a new data analysis method, and only
  merge it into the main branch if the method proves effective.
- **Commits.** A commit is a snapshot of changes in the project. Each commit
  records |html-dash| what changes were made, who made the changes, when they
  were made and a message describing why the changes were made. Commit
  messages should be clear and descriptive, as they serve as a record for
  others who may need to reproduce or build upon your work.

.. _installing-git:

Installing Git
===============================================================================

#. Go to `git-scm.com <https://git-scm.com/downloads>`_ and download the
   latest version for your operating system.
#. Run the installer.

   .. tab-set::
       :sync-group: operating-system

       .. tab-item:: Windows
           :sync: windows

           Double-click the downloaded ``.exe`` file and follow the on-screen
           instructions. Accept the default settings unless you have a specific
           reason to modify them..

       .. tab-item:: macOS
           :sync: macos

           Open the ``.dmg`` file, drag the Git application into your
           ``Applications`` folder, and follow any remaining instructions.

       .. tab-item:: Linux
           :sync: linux

           Open your terminal and use the following command based on your Linux
           distribution.

           .. tab-set::

               .. tab-item:: Ubuntu/Debian

                   .. code-block:: shell

                       sudo apt update && sudo apt install git

               .. tab-item:: Fedora/RHEL

                   .. code-block:: shell

                       sudo dnf install git

               .. tab-item:: Arch Linux

                   .. code-block:: shell

                       sudo pacman -S git

#. Verify the installation by opening a terminal or command prompt and type the
   following command:

   .. code-block:: shell

        git --version

With Git installed, you'll be able to synchronize your local work with a
remote repository on :ref:`about-github` (or another Git-based platform) and
start collaborating on open science projects.
