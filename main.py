import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('Progress bar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}%')
    bar.progress(i + 1)
    time.sleep(0.05)
    

'Done!'

# DataFrame, Chart-----
# st.write('DataFrame')
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.dataframe(df.style.highlight_max(axis=0))
# st.line_chart(df)


# Checkbox-----
# st.write('Display Image')
# if st.checkbox('Show Image'):
#     img = Image.open('年賀状_2022.jpg')
#     st.image(img, caption='年賀状', use_column_width=True)


# Selectbox-----
# option = st.selectbox(
#     'What number do you like?',
#     list(range(1, 11)),
# )
# 'Number you like is ', option, '.'


# Text_input-----
# text = st.text_input('What is your hobby?')
# 'Your hobby: ', text


# Slider-----
# condition = st.slider('How about you?', 0, 100, 50)
# 'Condition: ', condition


# expander-----
# expander1 = st.expander('FAQ')
# expander1.write('Question1')
# expander2 = st.expander('About us')
# expander2.write('https://www.yahoo.co.jp/')


# Sidebar layout-----
# text = st.sidebar.text_input('What is your hobby?')
# 'Your hobby: ', text


# 2column layout-----
# left_column, right_column = st.columns(2)
# button = left_column.button('display charactor in right column')
# if button:
#     right_column.write('Check button')


# マジックコマンド、マークダウン-----
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """