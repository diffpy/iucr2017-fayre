def differenceplot(recipe, baseline=0):
    """Nice plot of data, simulation and difference curve.
    """
    from matplotlib.pyplot import plot, setp, hlines
    cntb = recipe._contributions.values()[0]
    x = cntb.profile.x
    yobs = cntb.profile.y
    ycalc = cntb.evaluate()
    ydiff = yobs - ycalc
    rv = plot(x, yobs, 'bo', x, ycalc, 'r-', x, ydiff + baseline, 'g-')
    setp(rv[0], markeredgecolor='blue', markerfacecolor='none')
    hlines(baseline, x.min(), x.max(), linestyles='dashed')
    return rv
