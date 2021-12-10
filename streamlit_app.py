import streamlit as st
import pandas as pd
import pickle
import time

# import turicreate as tc

st.set_page_config(page_title="Element Solutions Recommender System", page_icon="🐞", layout="centered")

df = pd.read_csv('/Users/zhyarsozhyn/Downloads/df_filter_pre.csv')
chemdict = pickle.load(open("/Users/zhyarsozhyn/Downloads/chemdict.pkl", "rb"))
# model = tc.load_model("/Users/zhyarsozhyn/Downloads/RS.model")
dfS = pd.read_csv('/Users/zhyarsozhyn/Downloads/df_recommendation_item.csv')

@st.experimental_singleton()
def FilteringSol(ChemicalType, FlashPoint, PolarityValue):
  cond1 = df["Type"] == ChemicalType
  cond2 = df["Flash Point °C"] > FlashPoint
  cond3 = df["Polarity"] == PolarityValue
  allcond = cond1 & cond2 & cond3
  newdf = df["Product"][allcond]
  return newdf

def FilteringSur(ChemicalType, Functionality, Material_Base):
  cond1 = df["Type"] == ChemicalType
  cond2 = df["Surfactant Functionality"] == Functionality
  cond3 = df["Raw Material Base"] == Material_Base
  allcond = cond1 & cond2 & cond3
  newdf = df["Product"][allcond]
  return newdf

st.header("🐞 Element Solutions Recommender System!")
st.subheader('AI-Growth-Lab AAU')

st.sidebar.write(
    f"This app can help you to find or design your desirable products."
)

st.sidebar.write(
    f"[Read more](https://www.elementsolutionsinc.com/) about the company."
)

form = st.form(key="annotation")

cols = st.columns((1, 1))

chemical_type = cols[0].selectbox(
        "Chemicel type:", ["Solvent", "Surfactant"], index=1
)
if chemical_type == "Solvent":
    polarity = cols[1].selectbox("Polarity:", ['High Polarity', 'Medium Polarity', 'Low Polarity'], index=2)
    flash_point = st.slider("Minimum Flash Point:", 0, 130, 10)
    satisfying_list = FilteringSol(ChemicalType=chemical_type, FlashPoint=flash_point, PolarityValue=polarity)
else:
    desired_functionality = cols[1].selectbox("Desired Functionality:", ["Emulsifier", "Cleaning surfactantd"], index=1)
    material_base = st.selectbox("Material Base:", ["Synthetic", "Vegetable", "Vegetable-synthetix"], index=2)
    satisfying_list = FilteringSur(ChemicalType="Surfactant", Functionality=desired_functionality, Material_Base=material_base)


if st.button("Submit"):
    st.write("This is a list of chemicals satisfying your criteria: ")
    st.table(satisfying_list)
    if st.button("Recommendation Products"):
        # recommendation_item = model.get_similar_items(items=[430018], k=10)
        # dfS = pd.DataFrame(recommendation_item)
        # dfS = dfS.replace({"similar":chemdict})
        # dfS = dfS.replace({"productId":chemdict})
        st.write("This is a list of recommendation products: ")
        st.table(dfS)


# # An alias for our state
# state = st.session_state
# # A function to easily go from one step to another
# def change_step(next_step):
#     state = next_step
# # Let's initialize our session state
# if st.button("Submit"):
#     state = "init"
# # Step 1
# if state == "init":
#     st.write("This is a list of chemicals satisfying your criteria: ")
#     st.table(satisfying_list)
#     state = "load"
# # if st.button("Recommendation Products"):
# #     state = "load"
# # Step 2
# if state == "load":
#     st.button("Recommendation Products")
#     state = "upper"
# # # Step 3
# if state == "upper":
#     st.write("This is a list of recommendation products: ")
#     st.table(dfS)
# # # We print our data everytime
# # st.write(state.data)

