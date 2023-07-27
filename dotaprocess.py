import numpy as np
import os
import json


path = 'container_dataset/train_labels/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.json')]


def dotawrite(ex, angle=np.math.pi*2, enlarge=False):
    x1, y1 = "%.6f"%(ex[0]), "%.6f"%(ex[1])
    x2, y2 = "%.6f"%(ex[2]), "%.6f"%(ex[3])
    x3, y3 = "%.6f"%(ex[4]), "%.6f"%(ex[5])
    x4, y4 = "%.6f"%(ex[6]), "%.6f"%(ex[7])
    x_min = min(list(map(float, [x1, x2, x3, x4])))
    x_max = max(list(map(float, [x1, x2, x3, x4])))
    y_min = min(list(map(float, [y1, y2, y3, y4])))
    y_max = max(list(map(float, [y1, y2, y3, y4])))
    
    
    points = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    p_arr= np.array(points,dtype=np.float32)
    if enlarge:
        c,s=  np.cos(angle), np.sin(angle)
        r_matrix = np.array([[c, s],
                            [-s, c]])
        m_x, m_y = np.mean(p_arr, axis=0)
        
        p_arr[:, 0] -= m_x 
        p_arr[:, 1] -= m_y 
        p_arr = (p_arr@r_matrix)
        p_arr[:, 0] += m_x 
        p_arr[:, 1] += m_y 

        w = max(p_arr[:,0]) - min(p_arr[:,0])
        h = max(p_arr[:,1]) - min(p_arr[:,1])
        w_big = (x_max-x_min)/2
        h_big = (y_max-y_min)/2
        if w > h:
            w_big = max(w_big, h_big)
            h_big = min(w_big, h_big)
        else:
            w_big = min(w_big, h_big)
            h_big = max(w_big, h_big)

        points = [[m_x-w_big,m_y-h_big],[m_x+w_big,m_y-h_big],[m_x+w_big,m_y+h_big],[m_x-w_big,m_y+h_big]]
        r_matrix = np.array([[c, -s],
                            [s, c]])
        p_arr= np.array(points,dtype=np.float32)
        p_arr[:, 0] -= m_x 
        p_arr[:, 1] -= m_y 
        p_arr = (p_arr@r_matrix)
        p_arr[:, 0] += m_x 
        p_arr[:, 1] += m_y 
    
    out = ' '.join([' '.join(list(map(str,list(p_arr[i])))) for i in range(4)])
    return out + ' container 0\n'


os.makedirs("container-dota/train/anns/", exist_ok=True)

for idx, filename in enumerate(file_list_py):
    with open (path+filename, "r") as f:
        data = json.load(f)
        n_box = len(data['features'])
        txt_name = filename.replace('.json', '.txt')
        
        f=open(f"container-dota/train/anns/{txt_name}", 'w')
        
        for i in range(n_box):
            ex = list(map(float,data['features'][i]['properties']['object_imcoords'].split(',')))
            # angle = float(data['features'][i]['properties']['object_angle'])
            # assert angle>=0 , f"wrong angle! got {angle}"
            # rec = np.math.pi/2
            # n = int(angle/rec)
            # assert (angle-n*rec >= 0), (f"no rotate! got {angle-n*rec:.5f}")
            # # angle-(n+1)*rec
            # #  angle=angle
            dota = dotawrite(ex)
            f.write(dota)
