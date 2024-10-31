

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv')
S=list(df['SepalWidthCm'])
L=list(df['SepalLengthCm'])
K=list(df['PetalLengthCm'])
M=list(df['PetalWidthCm'])
fig = plt.figure(figsize = (10,10),dpi=100)
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)
ax1.plot(S,L,'r.', label = 'red dots')
ax2.plot(S,K,'b.', label = 'blue dots')
ax3.plot(S,M,'y.', label = 'yellow dots')
ax4.plot(M,K,'m.', label = 'purple dots')
ax5.plot(M,L,'g.', label = 'green dots')
ax6.plot(K,L,'c.', label = 'black dots')
plt.show()
