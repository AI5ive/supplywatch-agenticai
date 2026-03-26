# **Challenge Category**
Query‑to‑Insight Analytics Engineer  
(Project focus: Supply Chain Risk Management)

# **SupplyWatch: AI‑Driven Supplier Risk & Anomaly Detection**
A multi‑agent AI system that detects supplier risk early, analyzes contributing factors, and recommends mitigation actions through an automated, end‑to‑end workflow.

<img width="300" height="300" alt="SupplyWatch Logo_white background" src="https://github.com/user-attachments/assets/e77a519c-0087-4522-a7b9-9297ec0583fa" />

---

## **Short Description**
SupplyWatch helps supply chain teams identify supplier issues before they escalate. Using a chain of Copilot Studio agents orchestrated through Power Automate and Dataverse, the system evaluates risk, recommends actions, and delivers alerts directly to stakeholders.

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
_Link to demo video goes here_

---

## 📑 **PowerPoint Presentation**
_Link to presentation deck goes here_

---

## 📊 **Architecture Diagram**

<img width="1530" height="658" alt="SupplyWatch High Level Architecture" src="https://github.com/user-attachments/assets/e8c2b1f9-6c4e-4e85-a9e3-31debc78442a" />

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

## **Repository Structure**

---

## **Future Enhancements**
- Integrate external supplier data sources (ERP, quality systems, shipment tracking)  
- Add a Power BI dashboard for real‑time supplier risk visibility  
- Introduce a Forecasting Agent for predictive risk modeling  
- Enable Teams notifications once tenant limitations are resolved  
- Expand multi‑language support for global teams  
- Add Responsible AI monitoring for transparency and auditability  


