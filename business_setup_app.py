import streamlit as st

# Streamlit App Layout
st.title("LabFlow.AI Business Setup Checklist")

st.markdown("""
This interactive guide will help you go through the necessary steps to start and launch LabFlow.AI, set up marketing channels, and handle business fundamentals.
""")

# Step 1: DBA and Legal Structure
st.header("Step 1: Forming a DBA and Legal Structure")
with st.expander("Details"):
    st.markdown("""
    1. Choose your business name (LabFlow.AI).
    2. Check for name availability in your state or country.
    3. Register your DBA (Doing Business As) with your local authority.
    4. Obtain an EIN from the IRS if you're in the US for tax purposes.
    5. Open a business bank account using your DBA to separate personal and business finances.
    """)
start_dba = st.checkbox("Completed: Forming a DBA")

# Step 2: Marketing Channels
st.header("Step 2: Setting Up Marketing Channels (Apollo.io & LinkedIn Sales Navigator)")
with st.expander("Details"):
    st.markdown("""
    **LinkedIn Sales Navigator**
    1. Create an optimized LinkedIn profile and company page.
    2. Use Sales Navigator to target industries like healthcare, diagnostics, and biotechnology.
    3. Use job titles such as Lab Manager, Data Analysts, and Compliance Managers for outreach.

    **Apollo.io**
    1. Set up Apollo.io for outreach and prospecting.
    2. Filter for companies involved in laboratory operations and regulatory compliance.
    3. Run email campaigns targeting labs based on their size and sector.
    """)
start_marketing = st.checkbox("Completed: Setting Up Marketing Channels")

# Step 3: Developing Pricing Structure
st.header("Step 3: Developing a Pricing Structure")
with st.expander("Details"):
    st.markdown("""
    Based on your target market, you can use one of the following pricing strategies:
    - **Subscription-Based Pricing**: Offer tiers for small, medium, and large labs.
    - **Pay-Per-Report**: Charge based on the number of reports processed.
    - **Setup + Subscription**: Charge a setup fee for custom configurations, then charge a monthly subscription.
    """)
start_pricing = st.checkbox("Completed: Pricing Strategy")

# Step 4: Website and Marketing Materials
st.header("Step 4: Website Development and Marketing Materials")
with st.expander("Details"):
    st.markdown("""
    1. Register your website domain (e.g., labflow.ai).
    2. Develop a professional website to showcase services and testimonials.
    3. Create marketing content such as:
        - Sales Deck
        - Case Studies
        - Blog Posts
        - Explainer Videos
        - Webinars
    """)
start_website = st.checkbox("Completed: Website and Marketing Materials")

# Step 5: CRM Setup
st.header("Step 5: CRM Setup")
with st.expander("Details"):
    st.markdown("""
    1. Set up a CRM like HubSpot or Salesforce to manage leads and prospects.
    2. Automate email campaigns for lead nurturing.
    """)
start_crm = st.checkbox("Completed: CRM Setup")

# Step 6: Compliance and Security
st.header("Step 6: Compliance and Data Security")
with st.expander("Details"):
    st.markdown("""
    1. Ensure your app complies with HIPAA (US) and GDPR (UK/EU) for handling sensitive data.
    2. Implement encryption for data at rest and in transit.
    """)
start_compliance = st.checkbox("Completed: Compliance and Security Setup")

# Step 7: Launch Operations
st.header("Step 7: Operations Plan")
with st.expander("Details"):
    st.markdown("""
    1. Set up scalable cloud infrastructure (AWS, Azure, Google Cloud).
    2. Hire key staff for sales, customer support, and tech operations.
    3. Create customer support processes.
    """)
start_operations = st.checkbox("Completed: Launch Operations")

# Step 8: Financial Projections and Sales Strategy
st.header("Step 8: Financial Projections and Sales Strategy")
with st.expander("Details"):
    st.markdown("""
    1. Create financial projections for subscription fees, pay-per-report pricing, and custom solutions.
    2. Define your sales strategy for reaching key regions (US and UK).
    """)
start_sales = st.checkbox("Completed: Financial Projections and Sales Strategy")

# Summary Section
st.header("Progress Summary")
if start_dba and start_marketing and start_pricing and start_website and start_crm and start_compliance and start_operations and start_sales:
    st.success("🎉 Congratulations! You’ve completed all the steps for launching LabFlow.AI.")
else:
    st.warning("There are still some tasks to complete before launching.")

# Footer
st.markdown("""
---
Feel free to revisit any section if you need to complete specific tasks.
""")
