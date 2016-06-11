import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import numpy as np
import time
import datetime
import random
import sentiment2

py.sign_in('SamarthJain', 'zse4msy081')

stream_ids = tls.get_credentials_file()['stream_ids']
stream_id = stream_ids[1]
# Make instance of stream id object
stream_1 = go.Stream(
   token=stream_id,  # link stream id to 'token' key
   maxpoints=100     # keep a max of 80 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
   x=[],
   y=[],
   mode='lines+markers',
   stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Time Series')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.plot(fig, filename='python-streaming1',auto_open=False)

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()

# (*) Import module keep track and format current time


i = 0    # a counter
k = 5    # some shape parameter



while True:

    print "Entered while of Plots"
    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]
    y = sentiment2.main()
    # To update plot data
    print "X", x, " + Y ", y
    s.write(dict(x=x, y=y))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
    # time.sleep(5)  # desired time intervals
# Close the stream when done plotting
s.close()

#tls.embed('streaming-demos','12')

# x = [
#    datetime(year=2013, month=10, day=04),
#    datetime(year=2013, month=11, day=05),
#    datetime(year=2013, month=12, day=06)
#    ]
# while True:
#     y1 = random.random()
#     y2 = random.random()
#     y3 = random.random()
#     data = [
#         go.Scatter(x=x,y=[y1, y2, y3])
#     ]
#     py.plot(data)
#     time.sleep(1200)
