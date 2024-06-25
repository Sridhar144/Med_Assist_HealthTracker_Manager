def conversion(hist, user):
    params = {}
    rec = []
    for record in hist:
        obj = [
            record['timestamp'],
            record['app'],
            record['disease'],
            record['result'],
            record['probability'],
            record['message'],
        ]
        rec.append(obj)
    rec.reverse()
    sz = len(rec)
    params = {'records' : rec, 'size' : sz, 'user':user}
    return params