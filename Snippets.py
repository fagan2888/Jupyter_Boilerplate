# Import Clustering Data From Matlab, where data is in a struct
featureDict = sio.loadmat('../Preprocessing/features.mat', struct_as_record=False)
featureDict = featureDict['features'][0][0].__dict__    # Strange way to convert whatever was loaded into a dictionary
featureDict.pop('_fieldnames')                          # Remove fieldnames since keys have that info


# Convert matlab datenums to python datetime
mdt = 736739.479009309      # Matlab datenum
pdt = datetime.datetime.fromordinal(int(mdt)) + datetime.timedelta(days=mdt % 1) - datetime.timedelta(days=366)
pdt.isoformat(sep=' ')      # Print for verification


# Pretty print entire pandas data frame
with pd.option_context('display.max_rows', None, 'display.max_columns', 10):
    print(df)


# 5-minute average time series - not a rolling average, more like a downsample
valAvg = valSeries.resample("5min", closed='left').mean()

    
# Resample multiple time series where index is time and columns are the different series. 
# The result of this operation is a new frame where every n columns are averaged together.
testO = pd.DataFrame()
for i in range(20,30):
    testO[i] = [i-20]*20
testO.index = pd.date_range('1/1/2014', periods = 20, freq='min')
testGB = testO.T.groupby(testO.T.index // 3).mean().T

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print("---Original---")
    print(testO)
    print("\n---Grouping Index---")
    print(testO.T.index // 3)
    print("\n---New---")
    print(testGB)
