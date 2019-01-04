import maya.cmds as cmds
selec = cmds.ls(sl=True)
axes = ['X','Y','Z']
for i in selec:
    cmds.select(i,r=1)   
    state_viz1 = cmds.getAttr(i+'.visibility', l=False)
    state_viz2 = cmds.getAttr(i+'.visibility', l=True) 
    if not state_viz1 == True or state_viz2  == True:
        cmds.setAttr(i+'.visibility',l=False, k=True)
        cmds.setAttr(i+'.visibility',1)
         
    for axe in axes:
        state_trans = cmds.getAttr(i+'.translate'+axe, k=True)
        state_rotate= cmds.getAttr(i+'.rotate'+axe, k=True)
        state_scale = cmds.getAttr(i+'.scale'+axe, k=True)

        if not state_trans == True:
            cmds.setAttr(i+'.translate'+axe, l=False,k=True)
        if not state_rotate == True:
            cmds.setAttr(i+'.rotate'+axe, l=False,k=True)     
        if not state_scale == True:
            cmds.setAttr(i+'.scale'+axe, l=False,k=True)