# Save your Streamlit code into a file named ovetstreamlit.py
import streamlit as st

# ------------------ Hardcoded Lists ------------------

dog_breeds = sorted([
    "Beagle", "Boxer", "Bulldog", "Dachshund", "German Shepherd",
    "Golden Retriever", "Labrador Retriever", "Poodle", "Shih Tzu", "Yorkshire Terrier"
])

cat_breeds = sorted(["Domestic Shorthair", "American Shorthair", "Domestic Longhair", "Ragdoll",
    "Siamese", "Bengal", "Maine Coon", "British Shorthair", "Persian", "Russian Blue",
    "Sphynx", "Scottish Fold", "Exotic Shorthair", "Oriental Shorthair", "Burmese",
    "Devon Rex", "Himalayan", "Abyssinian", "Birman", "Norwegian Forest Cat"

])

minor_health_conditions = sorted([
    "Hairballs", "Diarrhea", "Food Sensitivity", "Anxiety", "Skin Issue",
    "Dental Issue", "Weight Management", "Urgent Care", "Vision Problem",
    "General Health", "Dehydration", "Gastroenteritis"
])

major_health_conditions = sorted([
    "Diabetes Mellitus", "Allergy", "Dental Issue", "Periodontal Disease",
    "Bone and Joint Issue", "Osteoarthritis", "Arthritis", "Heart Disease",
    "Metabolic Issue", "Underweight", "Cognitive Issue", "Brain Health Issue",
    "Liver Failure", "Liver Dysfunction", "Hepatitis", "Skin Issue",
    "Cushing's Syndrome", "Gastrointestinal Disorder", "Aging", "Immune Support",
    "Weight Management", "Urgent Care", "Hyperthyroidism", "Restorative Care",
    "Pancreatitis", "Kidney Problem", "Urinary Problem", "Cancer",
    "Food Sensitivity", "Hyperglycemia", "Anxiety", "Mental Health Disorder",
    "Hyperlipidemia", "Inflammatory Bowel Disease", "Inflammatory Mediators",
    "Obesity", "Seizure", "Oxalate Stones", "Struvite", "Proteinuria",
    "Epileptic", "Vision Problem", "Hypertension", "Heart Failure",
    "Fat Intolerant", "Gallbladder Disease", "Hypothyroidism", "General Health",
    "Atopic Dermatitis", "Adrenal Disorders", "Catabolic States",
    "Debilitation", "Dehydration", "Surgery"
])

cat_specific_conditions = sorted([
    "Hairballs", "PLE", "Lymphangiectasia", "Feline LUTS"
])

allergy_list = sorted([
    "Barley", "Beef", "Carrot", "Chicken", "Corn", "Dairy", "Duck", "Egg", "Fish", "Flaxseed",
    "Lamb", "Oat", "Pea", "Pork", "Potato", "Pumpkin", "Rice", "Salmon", "Soy", "Sweet Potato",
    "Tomato", "Turkey", "Wheat", "Brown Rice", "Coconut", "Chickpea", "Fava Beans", "Quinoa", "Sorghum", "Tapioca",
    "Black Beans", "Broccoli", "Algae", "Millet", "Venison", "Kangaroo", "Duck Liver", "Liver",
    "Rabbit", "Spinach", "Milk"
])

activity_levels = ["Active", "Not Active"]
life_stages = ["Growth", "Adult", "Senior"]

# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="Pet Nutrition Recommender", layout="centered")
st.title("🐾 Pet Nutrition Recommendation Tool")

# Gender selector with no pre-selection
has_gender = st.radio("Gender", options=["Male", "Female"], index=None)

# Species dropdown with placeholder
species = st.selectbox("Species", ["-- Select species --", "Dog", "Cat"])

breed_list = []
breed_name = "-- Select a breed --"

if species == "Dog":
    breed_list = dog_breeds
elif species == "Cat":
    breed_list = cat_breeds

if breed_list:
    breed_name = st.selectbox("Breed Name", ["-- Select a breed --"] + breed_list)

# Allergy selector with no pre-selection
has_allergy = st.radio("Allergies", options=["Yes", "No"], index=None)

# Allergy dropdown
selected_allergies = []
if has_allergy == "Yes":
    selected_allergies = st.multiselect("Allergies", allergy_list, placeholder="Choose an option")

# Lactation selector with no pre-selection
has_lactation = st.radio("Lactating", options=["Yes", "No"], index=None)

# Pregnant selector with no pre-selection
has_pregnant = st.radio("Pregnant", options=["Yes", "No"], index=None)

# ------------------ Main Form ------------------

with st.form("pet_form"):
    breed_size = st.selectbox("Breed Size", ["-- Select breed size --", "Small", "Medium", "Large"])
    life_stage = st.selectbox("Life Stage", ["-- Select life stage --"] + life_stages)
    activity_level = st.selectbox("Activity Level", ["-- Select activity level --"] + activity_levels)

    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, value=0.0)
    age = st.number_input("Age (months)", min_value=0, step=1, value=0)
    body_score = st.slider("Body Score (1-9)", min_value=1, max_value=9, step=1)

    # Major Health Conditions
    major_health_conditions_selected = st.multiselect("Major Health Conditions", major_health_conditions, placeholder="Choose an option")

    # Minor Health Conditions
    minor_health_conditions_selected = st.multiselect("Minor Health Conditions", minor_health_conditions, placeholder="Choose an option")

    # Cat-Specific Conditions (Conditional)
    cat_specific_conditions_selected = []
    if species == "Cat":
        cat_specific_conditions_selected = st.multiselect(
            "Cat-Specific Conditions",
            cat_specific_conditions,
            placeholder="Choose an option"
        )

    submit = st.form_submit_button("Get Recommendations")

# ------------------ Output ------------------

if submit:
    errors = []

    if species == "-- Select species --":
        errors.append("Please select a species.")
    if breed_name == "-- Select a breed --":
        errors.append("Please select a breed.")
    if breed_size == "-- Select breed size --":
        errors.append("Please select a breed size.")
    if life_stage == "-- Select life stage --":
        errors.append("Please select a life stage.")
    if activity_level == "-- Select activity level --":
        errors.append("Please select an activity level.")
    if has_allergy is None:
        errors.append("Please select whether the pet has allergies.")

    if errors:
        for err in errors:
            st.error(err)
    else:
        user_input = {
            "species": species,
            "breed": breed_name,
            "breed_size": breed_size,
            "life_stage": life_stage,
            "weight": weight,
            "body_score": body_score,
            "activity_level": activity_level,
            "major_health_conditions": major_conditions_selected,
            "minor_health_conditions": minor_health_conditions_selected,
            "cat_specific_conditions": cat_specific_conditions_selected,
            "allergy": has_allergy,
            "allergies": selected_allergies,
        }

        # Mock recommendations
        st.markdown("### 🍽️ Recommended Foods:")
        for food in [
            "Hill's Metabolic + Mobility",
            "Royal Canin Hypoallergenic",
            "Rayne Clinical Nutrition RSS"
        ]:
            st.write(f"- {food}")
