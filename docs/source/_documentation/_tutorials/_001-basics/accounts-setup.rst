.. Author: Akshay Mestry <xa@mes3.dev>
.. Created on: Saturday, November 02, 2024
.. Last updated on: Sunday, November 03, 2024

:og:title: Accounts Setup
:og:description: Setting up all the necessary accounts for Open Science.

.. _accounts-setup:

===============================================================================
Accounts Setup
===============================================================================

.. title-hero::
    :icon: fa-brands fa-github
    :summary:
        Set up essential accounts needed to contribute to Open Science. Follow
        these easy, step-by-step guides to create and configure the accounts
        required for contributing towards open science.

.. tags:: getting-started, open-science-101, github, orcid

.. contributors::
    :location: Chicago, IL
    :timestamp: November 03, 2024

    - :name: Akshay Mestry
    - :email: xa@mes3.dev
    - :headshot: https://avatars.githubusercontent.com/u/90549089?v=4
    - :github: https://github.com/xames3
    - :linkedin: https://linkedin.com/in/xames3
    - :orcid: https://orcid.org/0009-0000-4562-8983
    - :status: Open Source Maintainer

In the world of open science, certain digital tools and platforms are
indispensable for sharing research, collaborating with peers, and managing
your scientific identity. Before diving into your open science journey,
setting up accounts on some key platforms will empower you to fully
participate in this transparent, collaborative ecosystem. Below, we'll walk
through the importance of each account, real-world use cases, and practical
examples of how they are utilized in open science workflows.

-------------------------------------------------------------------------------
GitHub
-------------------------------------------------------------------------------

.. image:: https://github.blog/wp-content/uploads/2023/10/
   Collaboration-DarkMode-2.png?w=1200
    :alt: GitHub banner

:term:`GitHub` is one of the most powerful tools in the world of collaborative
research, open science, and software development. It's more than just a
platform for storing code |html-dash| it's a vibrant community where you can
contribute to projects, share data, and collaborate with fellow researchers
from all over the world. Whether you're a beginner or a seasoned coder, GitHub
provides the tools you need to manage projects, contribute to
:term:`Open Science`, and share your findings.

.. dropdown:: Importance for Open Science

    - **Version Control.** Keeps track of all changes to your code, making it
      easy to revert to previous versions if necessary. This is crucial in
      research projects where :term:`reproducibility` is key.

    - **Collaborative Research.** Enables multiple researchers to work
      together on the same project, with features like forking, pull requests,
      and issue tracking. For instance, a team of climate scientists may use
      GitHub to manage code for analyzing climate models. Each team member
      contributes code and reviews changes through pull requests.

    - **Open Access.** You can make your repositories public, allowing others
      to view, use, and contribute to your research. Example for this would be
      an ecologist sharing a Python package on GitHub that automates the
      analysis of satellite imagery, allowing others to replicate or build on
      the work.

At its core, GitHub is a hosting service for version control using Git. This
means it helps you track changes in your work, collaborate with others
seamlessly, and manage multiple versions of a project. Many of NASA's open
science projects, including the :term:`TOPS` :term:`SCHOOL` initiative, use
GitHub to share their work and invite contributions from the global community.
So, setting up a GitHub account is the first step toward being part of this
exciting, inclusive movement.

Let's walk through how to create your personal GitHub account and get started
with open science!

.. note::

    If you already have a GitHub account, you can skip this guide and checkout
    things to do to :ref:`secure-your-github-account` below.

Creating GitHub Account
===============================================================================

#. Go to `GitHub`_.
#. In the upper-right corner of the page, click on the **Sign up** button to
   start creating your personal account. GitHub will guide you through the
   process, one step at a time.
#. You will be asked for a **username**, **email address**, and to create a
   **password**.
#. Once you've entered your details, :term:`GitHub` will send a verification
   email to the address you provided.
#. Check your inbox (and your spam folder if you don't see it) and click the
   link to verify your email address.
#. Without verifying your email, you won't be able to perform certain tasks
   like creating repositories, so this step is important!
#. You'll be asked to complete a simple CAPTCHA (a quick task to confirm
   you're not a robot). Just follow the instructions, and you're good to go.
#. GitHub will prompt you to choose a plan. For most users just starting with
   :term:`Open Science`, the **Free** plan is more than enough. You can always
   upgrade later if you need advanced features like private repositories, but
   for now, you're all set with the free option!
#. Once your account is set up, you'll land on your GitHub dashboard. This is
   your home base for creating projects, exploring repositories, and
   contributing to open science. GitHub offers a helpful tutorial called
   "`Hello World <https://docs.github.com/en/get-started/start-your-journey/
   hello-world>`_" to get you started with the basics |html-dash| like
   creating your first repository, etc.

.. image:: https://octodex.github.com/images/NUX_Octodex.gif
    :align: center
    :alt: GitHub Octocat
    :class: transparent-border
    :width: 500

But before you move on, take a moment to congratulate yourself. You've just
taken a significant step toward being part of the open science community!

.. _secure-your-github-account:

Securing Your GitHub Account
===============================================================================

GitHub is an integral platform for collaborative research and open-source
projects, but with this openness comes the need for robust security measures.
By following best practices, you can ensure your research and data are
protected against unauthorized access. As of March 2023, GitHub required all
users who contribute code on `GitHub`_ to enable one or more forms of
two-factor authentication (2FA). Here's a detailed guide on securing your
GitHub account. All the security settings are accessible using the same steps.

- Navigate to Security Settings by clicking on to your
  :menuselection:`Profile --> Settings --> Password and authentication`

.. carousel::
    :show_controls:
    :show_fade:

    .. image:: ../../../_assets/guides/github-secure-profile.png
        :alt: Navigate to your profile - GitHub
        :class: transparent-border no-rounded-border

    .. image:: ../../../_assets/guides/github-secure-settings.png
        :alt: Select Settings - GitHub
        :class: transparent-border no-rounded-border

    .. image:: ../../../_assets/guides/github-secure-password.png
        :alt: Choose Password and authentication - GitHub
        :class: transparent-border no-rounded-border

.. tab-set::

    .. tab-item:: Two-factor Authentication (2FA)

        We strongly recommend that you configure 2FA for your account. 2FA is
        an extra layer of security that can help keep your account secure.
        Two-factor Authentication (2FA) adds an extra layer of security to
        your GitHub account by requiring a second form of verification beyond
        just your password. Here's how to set it up:

        .. image:: ../../../_assets/guides/github-secure-2fa.png
            :align: center
            :alt: Two-factor authentication - GitHub
            :scale: 60

        - Under the "Two-factor authentication" section, click the button to
          begin the setup process. Choose your authentication method
          :term:`GitHub` offers several 2FA options [#]_.
        - Follow the setup instructions and remaining prompts to complete the
          2FA setup. Ensure you test the 2FA method to confirm it's working
          properly.

    .. tab-item:: Adding a Passkey

        You can add passkeys to your account so that you can sign in safely
        and easily, without requiring a password and two-factor
        authentication. You can also use passkeys when performing a sensitive
        action (sudo mode), or to authenticate a password reset.

        Passkeys allow you to sign in securely to GitHub in your browser
        without having to input your password. If you use two-factor
        authentication (2FA), passkeys satisfy both password and 2FA
        requirements, so you can complete your sign in with a single step. If
        you don't use 2FA, using a passkey will skip the requirement to verify
        a new device via email. You can also use passkeys for sudo mode and
        resetting your password.

        Passkeys are pairs of cryptographic keys (a public key and a private
        key) that are stored by an authenticator you control. The
        authenticator can prove that a user is present and is authorized to
        use the passkey.

        .. image:: ../../../_assets/guides/github-secure-passkeys.png
            :align: center
            :alt: Passkeys - GitHub
            :scale: 60

        - Under the "Passkeys" section, click the button which says "Add a
          passkey" to begin the a process.
        - Follow the setup instructions and remaining prompts to complete the
          setup. [#]_ At the prompt, follow the steps outlined by the passkey provider.
        - On the next page, review the information confirming that a passkey
          was successfully registered, then click Done.

    .. tab-item:: Connect with SSH |badge-new|

            You can access and write data in repositories on GitHub using SSH
            (Secure Shell Protocol). When you connect via SSH, you
            authenticate using a private key file on your local machine. When
            you set up SSH, you will need to generate a new private SSH key
            and add it to the SSH agent. You must also add the public SSH key
            to your account on GitHub before you use the key to authenticate
            or sign commits.

            `Learn more <https://docs.github.com/en/authentication/connecting
            -to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to
            -the-ssh-agent>`_ |chevron-right|

            .. tip::

                Using the SSH protocol, you can connect and authenticate to
                remote servers and services. With SSH keys, you can connect to
                GitHub without supplying your username and personal access
                token at each visit. You can also use an SSH key to sign
                commits.

-------------------------------------------------------------------------------
ORCID
-------------------------------------------------------------------------------

Next, you'll learn how to create your :term:`ORCID` account, an important step
to ensure that your research and contributions are easily identifiable and
accessible in the Open Science community. Don't worry if this is your first
time doing this |html-dash| the process is straightforward, and this guide will help you through each step. Before we dive into the steps, let's talk
about why having an ORCID account is important.

:term:`ORCID` provides a unique, persistent identifier for researchers,
ensuring that your contributions are correctly attributed to you, regardless
of any changes :term:`Open Science`, where collaboration and transparency are
key. Your ORCID profile becomes your digital fingerprint in the world of
research, linking your work to your name in a global, accessible database.

Creating ORCID Account
===============================================================================

#. Go to `ORCID`_.
#. You'll see a form asking for some basic information. No worries, this will
   only take a minute or two. Enter your information like your **first** and
   **last** name, **primary email address** (this is where all your
   notifications will be sent), possibly a **secondary email address**
   (optional but recommended, to ensure you don't lose access in case you
   forget your credentials).
#. Next would be the password, make sure your password is something
   memorable but secure. Instructions about the password requirements would be
   mentioned while entering the password.
#. Before you complete the registration, you'll need to agree to ORCID's terms.
   These are pretty straightforward and ensure that your data is used
   responsibly.
#. Now that your account is created, ORCID will send a verification email to
   primary email address you provided. It's important to verify your email to
   complete the setup. Check your inbox (and your spam folder if you don't see
   it) and click the link to verify your email address.

.. tip::

    Set your visibility preferences. :term:`ORCID` gives you control over the
    privacy of your information. You can set your profile to be:

    - **Public.** Anyone can see your information.
    - **Limited.** Only trusted parties (like your institution) can view your
      profile.
    - **Private.** Only you can see your information.

    It is best to keep it **Public** to maximize visibility for your work in
    :term:`Open Science`, but you can always change it later.

Make the Most of Your ORCID Account
===============================================================================

Now that you've created and set up your ORCID account, you're ready to start
using your :term:`ORCID` ID in your research. Include it in your **CV**,
**Research papers**, **Articles**, **Conference presentations** and **Grant
applications**. This unique identifier will ensure that all your work is
properly attributed to you, wherever it's shared.

Personalizing your ORCID account is crucial in making sure your ORCID profile
represents you well. The more information you provide, the easier it will be
for collaborators and institutions to find you and recognize your work. ORCID
supports integration with various platforms, including :term:`GitHub` and
LinkedIn. You can link your ORCID profile to your GitHub account to create a
cohesive professional identity across platforms.

.. figure:: ../../../_assets/guides/orcid-github-link.png
    :align: center
    :alt: Link ORCID with GitHub
    :class: transparent-border no-rounded-border

    ORCID integrated with GitHub account.

Your ORCID profile is a living document. As your career progresses, be sure to
keep it updated with your latest contributions, projects, and affiliations.
This is especially important in :term:`Open Science`, where collaboration and
visibility are key. Set a reminder to check and update your profile every few
months. That way, your information stays fresh and accurate.

With your ORCID account ready, you're now one step closer to engaging fully
with the Open Science community. Remember, :term:`Open Science` is all about
transparency, accessibility, and collaboration. By taking the time to set up
your ORCID account, you're contributing to a global movement dedicated to
making science open to all.

.. rubric:: References
    :heading-level: 2

.. [#] Learn more about various ways of `Configuring two-factor authentication
       <https://docs.github.com/en/authentication/securing-your-account-with
       -two-factor-authentication-2fa/configuring-two-factor-authentication>`_.
.. [#] Learn more about `Adding a passkey to your account <https://docs.github.
       com/en/authentication/authenticating-with-a-passkey/
       managing-your-passkeys#adding-a-passkey-to-your-account>`_.
