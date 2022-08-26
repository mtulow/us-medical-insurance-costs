import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('colheader_justify', 'center')

dt = pd.read_csv('us-medical-insurance-costs/insurance.csv')
df = dt.head(10)

# Simply executing 'df' now will show the same output as the following code does, except to show the table within this article we need to render it as HTML.

css = '''
        <html>
          <link rel="stylesheet" type="text/css" href="df_style.css"/>
          <body>
            {table}
          </body>
        </html>
      '''

# OUTPUT AN HTML FILE
with open("index.html","w") as fp:
    fp.write(css.format(table=df.to_html(classes=["dataframe", "table"])))