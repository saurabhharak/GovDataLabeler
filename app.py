import base64
import streamlit as st
import pandas as pd

# Define Data Source Codes and Sector Codes
data_source_codes = {
    'CABSEC': 'Cabinet Secretariat',
    'CAG': 'Comptroller & Auditor General',
    'DAE': 'Department of Atomic Energy',
    'DOS': 'Department of Space',
    'ECI': 'Election Commission of India',
    'HCDELHI': 'HIGH COURT OF DELHI',
    'MOA': 'Ministry of Agriculture',
    'MCF': 'Ministry of Chemicals & Fertilizers',
    'MOCA': 'Ministry of Civil Aviation',
    'MOCOAL': 'Ministry of Coal',
    'MOCI': 'Ministry of Commerce & Industry',
    'MOCIT': 'Ministry of Communications & Information Tech.',
    'MOCF&PD': 'Ministry of Consumer Aff., Food, & Public Dist.',
    'MCA': 'Ministry of Corporate Affairs',
    'MOCULT': 'Ministry of Culture',
    'MOD': 'Ministry of Defence',
    'MDONER': 'Ministry of Development of North Eastern Region',
    'MDWS': 'Ministry of Drinking Water and Sanitation',
    'MOES': 'Ministry of Earth Sciences',
    'MOEF': 'Ministry of Environment & Forests',
    'MEA': 'Ministry of External Affairs',
    'MOF': 'Ministry of Finance',
    'MOFPI': 'Ministry of Food Processing Industries',
    'MOHFW': 'Ministry of Health & Family Welfare',
    'MHI&PE': 'Ministry of Heavy Industry & Public Enterprises',
    'MHA': 'Ministry of Home Affairs',
    'MOHUA': 'Ministry of Housing & Urban Poverty Alleviation',
    'MHRD': 'Ministry of Human Resource Development',
    'MOI&B': 'Ministry of Information & Broadcasting',
    'MOL&E': 'Ministry of Labour & Employment',
    'MOLJ': 'Ministry of Law & Justice',
    'MSME': 'Ministry of Micro, Small and Medium Enterprises',
    'MOM': 'Ministry of Mines',
    'MMA': 'Ministry of Minority Affairs',
    'MNRE': 'Ministry of New & Renewable Energy',
    'MPR': 'Ministry of Panchayati Raj',
    'MPA': 'Ministry of Parliamentary Affairs',
    'MPPP': 'Ministry of Personnel, Public Grievances & Pensions',
    'MPNG': 'Ministry of Petroleum & Natural Gas',
    'MP': 'Ministry of Power',
    'MR': 'Ministry of Railways',
    'MORTH': 'Ministry of Road Transport & Highways',
    'MRD': 'Ministry of Rural Development',
    'MST': 'Ministry of Science & Technology',
    'MS': 'Ministry of Shipping',
    'MSJE': 'Ministry of Social Justice & Empowerment',
    'MOSPI': 'Ministry of Statistics & Programme Implementation',
    'MSTL': 'Ministry of Steel',
    'MT': 'Ministry of Textiles',
    'MOT': 'Ministry of Tourism',
    'MTA': 'Ministry of Tribal Affairs',
    'MOUD': 'Ministry of Urban Development',
    'MWR': 'Ministry of Water Resources',
    'MWCD': 'Ministry of Women & Child Development',
    'MYAS': 'Ministry of Youth Affairs & Sports',
    'PC': 'Planning Commission',
    'PRES': 'President',
    'PMO': "Prime Minister's Office",
    'VP': 'Vice-President'
}



sector_codes = {
    'AGRI': 'Agriculture',
    'ANML': 'Animal Husbandry and Fisheries',
    'BNK': 'Banking',
    'CENS': 'Census',
    'CLMT': 'Climate & Weather',
    'CMDB': 'Commodity Boards',
    'COMR': 'Commerce',
    'CAFF': 'Consumer Affairs',
    'COVID': 'Covid',
    'CRIME': 'Crime',
    'CULT': 'Culture and Tourism',
    'DEMO': 'Demographics',
    'DIGINF': 'Digital Infrastructure',
    'ECON': 'Economy',
    'ELECT': 'Elections',
    'ENRG': 'Energy',
    'EXTAFF': 'External Affairs',
    'FINCL': 'Financial Inclusion',
    'FAGRI': 'Food and Agriculture',
    'FORWLD': 'Forestry and Wildlife',
    'GEN': 'General',
    'GOVSCM': 'Government Schemes',
    'HLTH': 'Health',
    'HSNG': 'Housing',
    'IND': 'Industries',
    'JUST': 'Justice',
    'NSS': 'National Sample Survey',
    'NATDIS': 'Natural Disasters',
    'OTHER': 'Other',
    'PETGAS': 'Petroleum and Gas',
    'RURALDEV': 'Rural Development',
    'SATIMG': 'Satellite Imagery Data',
    'SCI': 'Science',
    'SOCIOECO': 'Socio Economic',
    'TRANS': 'Transportation',
    'BUDGET': 'Union Budget',
    'WTR': 'Water'
}

#Granularity_values = ["District","State","Tehsil","Other Level", "India","Assembly Constituency","Point Level","Gram Panchayat","Block","Sub-District","Village","Country"]
 



# Short namings for Granularity_values
granularity_short_codes = {
    'District': 'DIS',
    'State': 'STA',
    'Tehsil': 'TEH',
    'Other Level': 'OTH',
    'India': 'IND',
    'Assembly Constituency': 'AC',
    'Point Level': 'PL',
    'Gram Panchayat': 'GP',
    'Block': 'BL',
    'Sub-District': 'SD',
    'Village': 'VIL',
    'Country': 'CTRY'
}
# frequency_values = ['Yearly', 'Weekly', 'Quinquennial', 'Daily', 'Fortnightly', 'Monthly', 'Seasonally', 'Other / One Time']
 

# Short namings for frequency_values
frequency_short_codes = {
    'Yearly': 'Y',
    'Weekly': 'W',
    'Quinquennial': 'Q',
    'Daily': 'D',
    'Fortnightly': 'F',
    'Monthly': 'M',
    'Seasonally': 'S',
    'Other / One Time': 'O'
}


# Read counter from file
def read_counter():
    try:
        with open('counter.txt', 'r') as f:
            counter = int(f.read())
    except FileNotFoundError:
        counter = 1  # Starting counter value
    return counter

# Update and save counter to file
def update_counter(counter):
    with open('counter.txt', 'w') as f:
        f.write(str(counter))

# Generate unique dataset IDs
def generate_dataset_id(counter):
    return f'DID{counter:03}'

# Generate dataset names
def generate_dataset_name(data_source_code, sector_code, start_year, end_year, dataset_id, granularity, frequency):
    granularity_short = granularity_short_codes.get(granularity, 'UNK')
    frequency_short = frequency_short_codes.get(frequency, 'UNK')
    return f'{data_source_code}-{sector_code}-{granularity_short}-{frequency_short}-{dataset_id}'

# List to store existing dataset names
existing_dataset_names = []

# Check if dataset name is unique
def check_dataset_name_uniqueness(dataset_name):
    return dataset_name not in existing_dataset_names


def generate_download_link(mapped_dataset):

    csv_file = mapped_dataset.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/xlsx;base64,{b64}" download="mapped_dataset.xlsx">Download</a>'
    st.success('Download Mapped Dataset')
    st.markdown(href, unsafe_allow_html=True) 

# Streamlit App
def main():
    st.title('Gov Data Labeler')
    
    # Read counter from file
    counter = read_counter()
    
    # User input: Data Source
    data_source = st.selectbox('Select Data Source', list(data_source_codes.values()))
    data_source_code = next(code for code, name in data_source_codes.items() if name == data_source)
    
    # Generate dataset name
    dataset_id = generate_dataset_id(counter)
    
    # User input: Sector
    sector = st.selectbox('Select Sector', list(sector_codes.values()))
    sector_code = next(code for code, name in sector_codes.items() if name == sector)
    
    # User input: Start Year
    start_year = st.number_input('Enter Start Year', min_value=2000, max_value=2100, value=2022)
    
    # User input: End Year
    end_year = st.number_input('Enter End Year', min_value=start_year, max_value=2100, value=2022)
    
    # User input: Granularity
    granularity = st.selectbox('Select Granularity', list(granularity_short_codes.keys()))
    
    # User input: Frequency
    frequency = st.selectbox('Select Frequency', list(frequency_short_codes.keys()))
    
    # Generate dataset name
    dataset_id = generate_dataset_id(counter)  # Update with your actual counter
    dataset_name = generate_dataset_name(data_source_code, sector_code, start_year, end_year, dataset_id, granularity, frequency)
    
    # User input: Original Dataset Name
    original_dataset_name = st.text_input('Enter Original Dataset Name')
    
    # Check if the dataset name is unique
    is_unique = check_dataset_name_uniqueness(dataset_name)  # Implement this function
    
    # Display generated dataset name
    st.write('Generated Dataset Name:')
    st.write(dataset_name)
    
    # Display warning/error if dataset name is not unique
    if not is_unique:
        st.warning('Dataset name is not unique. Please generate a new name.')
    
    # Save dataset info to Excel
    if st.button('Save to Excel') and is_unique:
        data = {
            'Dataset Name': [dataset_name],
            'Data Source': [data_source],
            'Sector': [sector],
            'Start Year': [start_year],
            'End Year': [end_year],
            'Granularity': [granularity],
            'Frequency': [frequency],
            'Original Dataset Name': [original_dataset_name]
        }
        df = pd.DataFrame(data)
        #df.to_excel('dataset_info.xlsx', index=False)
        
        # Update and save counter to file
        counter += 1
        update_counter(counter)
        generate_download_link(df)
        # Clear user inputs
        st.success('Dataset information saved to Excel.')
        data_source = ''
        sector = ''
        start_year = 2022  # Reset to default year
        end_year = 2022
        granularity = ''
        frequency = ''
        original_dataset_name = ''
    
if __name__ == '__main__':
    main()

