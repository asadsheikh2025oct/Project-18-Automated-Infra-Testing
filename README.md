# Azure Infrastructure-as-Code (IaC) Validation Framework

## 🚀 Overview

This project demonstrates a "Shift Right" testing strategy for Azure Infrastructure. It uses **Bicep** for resource provisioning and a **Python-based testing suite** to validate the live configuration of resources post-deployment. This ensures that the "As-Built" infrastructure matches the security policies defined by the organization.

## 🛠️ Tech Stack

* **Infrastructure:** Azure Bicep
* **Testing Framework:** Pytest
* **Cloud SDK:** Azure SDK for Python (`azure-mgmt-storage`)
* **Orchestration:** Azure DevOps Pipelines
* **Reporting:** JUnit XML / Azure Test Plans

## 🏗️ Project Architecture

The project follows a three-stage automated pipeline:

1. **Validation Stage:** Syntactic check of Bicep templates using `az bicep build`.
2. **Deployment Stage:** Incremental deployment of an Azure Storage Account to a target Resource Group.
3. **Testing Stage:** A custom Python suite authenticates via the Pipeline's Service Connection to verify security properties (e.g., Public Access, TLS version, HTTPS requirements).

## 🧪 Automated Tests

The Python test suite (`test_infrastructure.py`) performs the following assertions on live resources:

* **Public Access:** Ensures `allowBlobPublicAccess` is set to `false`.
* **Encryption:** Validates `supportsHttpsTrafficOnly` is `true`.
* **Modern Protocols:** Confirms `minimumTlsVersion` is set to `TLS1_2`.

## 📈 Pipeline Visualization

The Azure DevOps pipeline is configured to publish results to the **Tests Dashboard**. Even if a deployment succeeds, the pipeline will **fail** if the Python assertions do not pass, preventing insecure infrastructure from remaining in the environment.

## 📝 How to Use

1. **Clone the repo.**
2. **Configure Azure DevOps:** Create a Service Connection (`sc-project18`).
3. **Run the Pipeline:** Trigger `azure-pipelines.yml`.
4. **Validate:** Check the "Tests" tab in your Pipeline run to see the pass/fail breakdown of your live infrastructure.

---
