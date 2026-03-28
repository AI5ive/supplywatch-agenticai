# **Challenge Category**
Query‑to‑Insight Analytics Engineer  
(Project focus: Supply Chain Risk Management)

# **SupplyWatch: A Multi‑Agent, Orchestrated AI System for Supplier Risk Detection**
Agentic AI for proactive supplier management: detect early risks, understand the drivers, act with confidence, and ensure governance through orchestrated Copilot Studio agents.

<img width="300" height="300" alt="SupplyWatch Logo_white background" src="https://github.com/user-attachments/assets/e77a519c-0087-4522-a7b9-9297ec0583fa" />

---

## **Short Description**
SupplyWatch is an Agentic AI system built on Microsoft Power Platform that transforms how supply chain teams detect and respond to supplier risk.

Four specialized Copilot Studio agents work autonomously in sequence, each with a defined role: the Intake Agent normalizes submissions, the Analysis Agent scores risk and explains drivers, the Action Agent dispatches alerts and recommendations, and the Governance Agent closes the loop with compliance review and follow-up.

Every agent decision is logged to Dataverse, giving supply chain leaders complete traceability across the pipeline. Built on Copilot Studio, Power Automate, Dataverse, Power Apps, and Azure OpenAI, SupplyWatch delivers early detection, clear explanations, actionable recommendations, and automated governance in one intelligent system.

We are orchestrating risk detection that's modern, safe, and reliable.

---

## **Problem**
Supplier risk signals are scattered across delivery logs, quality reports, operational anomalies, and external indicators.  
Because these signals live in different systems, early detection becomes slow, inconsistent, and reactive.

---

## **Solution**
SupplyWatch unifies supplier signals and automates risk evaluation using four specialized Copilot Studio agents:

- **Intake Agent** – Normalizes and structures supplier issue reports  
- **Analysis Agent** – Evaluates severity, risk score, and contributing factors  
- **Action Agent** – Generates recommended mitigation actions and sends email alerts  
- **Governance Agent** – Ensures compliance and finalizes case resolution  

Power Apps provides the intake UI, Dataverse acts as the state machine, and Power Automate orchestrates the agent‑to‑agent workflow.  
Email is used for enterprise‑safe delivery due to tenant restrictions on Teams apps.

---

## 🎥 **Demo Video**

[Watch the SupplyWatch Demo on YouTube](https://youtu.be/UGtcylRmUVg)
---

## 📑 **PowerPoint Presentation**
[SupplyWatch_Final_Presentation.pptx](https://github.com/user-attachments/files/26296265/SupplyWatch_Final_Presentation.pptx)

---

## 📊 **Architecture Diagram**

<img width="1376" height="768" alt="SupplyWatch High Level Architecture2" src="https://github.com/user-attachments/assets/f6cf30e8-5c2b-4dfc-8fca-2b2291ad93cb" />

---

## **Multi‑Agent Architecture**
SupplyWatch uses four Copilot Studio agents, each triggered by Dataverse state transitions:

1. **Intake Agent**  
   - Structures raw supplier issue submissions  
   - Updates Dataverse and sets CaseStatus → *Analyzing*

2. **Analysis Agent**  
   - Generates risk score, severity, and contributing factors  
   - Updates Dataverse and sets CaseStatus → *ActionRequired*

3. **Action Agent**  
   - Produces recommended mitigation actions  
   - Sends email alerts  
   - Updates Dataverse and sets CaseStatus → *AwaitingGovernance*

4. **Governance Agent**  
   - Validates compliance and policy alignment  
   - Finalizes case resolution  
   - Updates CaseStatus → *Completed*

---

## **End‑to‑End Orchestration**



Dataverse acts as the **state machine**, and Power Automate orchestrates the entire workflow based on **CaseStatus** transitions.

---

## **Core Tech Stack**

### **Power Platform**
- Power Apps – Case intake UI  
- Dataverse – Case storage + state transitions  
- Power Automate – Multi‑agent orchestration + email alerts  
- Copilot Studio – Four Azure OpenAI‑powered agents  

### **Azure**
- Azure OpenAI (via Copilot Studio) – LLM reasoning for all agents  

### **Delivery**
- Email (replacing Teams Adaptive Cards due to tenant limitations)

---

## **Team Roles**

### **Chichi Iwuorie — Team Lead / TPM / Architect**
- Multi‑agent architecture  
- Action & Governance Agents  
- Orchestration flows  

### **CJ Johnson — Agent Engineering**
- Intake & Analysis Agents  
- Power Automate flows  
- Data normalization logic  

### **Giselle Carvalho — Power Apps & UX**
- Power Apps UI  
- Dataverse integration  
- Visual polish for demo  

### **Suliat Ogunneye — Storytelling & Demo Production**
- Demo script  
- Presentation flow  
- Responsible AI framing  

### **Ryan Rydalch — Technical Advisor**
- Architecture review  
- Data modeling and Dataverse schema    
- Testing & validation  

---

## **Key Learnings**
- **Tenant limitations shaped the architecture.**  
  - GoDaddy → Microsoft migration blocked Teams App Catalog.  
  - Power Automate’s Flow Bot could not be installed.  
  - Fabric capacity could not be provisioned.  
  - Teammates on free trials could not join Fabric workspaces.  
  These constraints required pivoting from Teams + Fabric to **email delivery** and **Dataverse‑driven orchestration**.

- **Dataverse is a powerful state machine** when paired with Power Automate.

- **Copilot Studio agents perform best with strict JSON schemas** and consistent prompt structure.

- **Multi‑agent systems require clear state transitions** to avoid orchestration conflicts.

---

## **Responsible AI**
- No PII stored or processed  
- Transparent risk scoring  
- Human‑in‑the‑loop governance  
- Auditability through Dataverse logs  
- Prompts aligned with Microsoft Responsible AI guidelines  

---

## **Future Enhancements**
- Integrate external supplier data sources (ERP, quality systems, shipment tracking)  
- Add a Power BI dashboard for real‑time supplier risk visibility  
- Introduce a Forecasting Agent for predictive risk modeling  
- Enable Teams notifications once tenant limitations are resolved  
- Expand multi‑language support for global teams  
- Add Responsible AI monitoring for transparency and auditability  


