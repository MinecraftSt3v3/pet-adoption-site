# CAPSTONE: [Chico-State-Marketplace](http://www.chicostatemarketplace.com) ![alt text](https://img.shields.io/github/actions/workflow/status/MinecraftSt3v3/Chico-State-Marketplace/github-actions-demo.yaml?label=Testing)

## Overview
Chico State Marketplace is a robust web application designed exclusively for students and faculty members of Chico State. With stringent email authentication protocols, the platform ensures a secure and trustworthy online marketplace, free from fraudulent activities and dubious individuals. Developed using the Django framework and styled with tailwind CSS, the application offers a seamless user experience, allowing users to post, delete, and message about their items while ensuring maximum safety and privacy.

In addition, the Chico State Marketplace offers an intelligent filtering mechanism, enabling users to sort through posts based on their major, thereby enhancing the relevance of the platform to the educational community. The ultimate goal of the application is to provide a safe and convenient online marketplace tailored to meet the unique needs of Chico State students and faculty, thereby setting it apart from other generic marketplaces like Facebook Marketplace.

This project involves the implementation of automation through Github Actions to establish a seamless Continuous Integration/Continuous Delivery pipeline. By utilizing this approach, I have successfully minimized testing duration while enhancing the efficacy of the testing process. As part of the workflow, once the testing phase is concluded and the requisite tests are passed, a Docker image will be constructed and seamlessly delivered from the workflow to the Google Cloud Platform (GCP) registry.


## Start Project Steps


1. start the tailwind server
    - python3 manage.py tailwind start
2. Start the manage.py run server
    - python3 manage.py runserver
