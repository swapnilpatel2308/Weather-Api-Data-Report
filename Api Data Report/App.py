import matplotlib.pyplot as plt
import json
import datetime
from windrose import WindroseAxes
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import json 
import requests

def Create_PDF(farmername,farmname,latitude,longitude):
    farmername = str(farmername)
    farmname = str(farmname)
    latitude = str(latitude)
    longitude = str(longitude)
    
    api_kry = 'ENTER YOUR API KEY'

    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'+latitude+'%2C'+longitude+'?unitGroup=metric&key='+api_kry+'&contentType=json'

    r = requests.get(url)

    data = r.json()

    # f = open('data.json')
    # data = json.load(f)


    filename = "report.pdf"
    p = PdfPages(filename)


    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)
    fig.suptitle("A Report On Soil And Air Quality",fontsize=16)

    # ax.text(0.5, 0.5, 'SAAMS', transform=ax.transAxes,fontsize=150, color='gray', alpha=0.5,ha='center', va='center', rotation=30)


    ax.text(-10, 90, f'Farmer Name : {farmername}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')


    ax.text(-10, 70, f'Farm Name : {farmname}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    date = (datetime.datetime.fromtimestamp(data['currentConditions']['datetimeEpoch']).strftime('%Y-%m-%d'))
    ax.text(-10, 50, f'Date : {date}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    location = data['resolvedAddress']
    ax.text(-10, 30, f'Location : {location}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    timezone = data['timezone']
    ax.text(-10, 10, f'Timezone : {timezone}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')


    ax.set(xlim=(0, 100), ylim=(0, 100))
    plt.grid(False)
    plt.axis('off')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)

    # import current data graphs

    current = data['currentConditions']


    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)
    fig.suptitle("Current Situation Data",fontsize=16)

    # time
    dateandtime = (datetime.datetime.fromtimestamp(current['datetimeEpoch']).strftime('%Y-%m-%d %H:%M:%S'))
    ax.text(-10, 90, f'Current Date And Time \n {dateandtime}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    temp = current['temp']
    ax.text(31, 90, f'Current Temperature in C \n                 {temp}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    humidity = current['humidity']
    ax.text(75, 90, f'Current Humidity in % \n                  {humidity}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    dew = current['dew']
    ax.text(-10, 65, f'Current Dew  \n     {dew}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    windspeed = current['windspeed']
    ax.text(31, 65, f'Current Wind Speed in Km/h  \n                   {windspeed}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    pressure = current['pressure']
    ax.text(75, 65, f'Current Pressure in Pa \n              {pressure}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    visibility = current['visibility']
    ax.text(-10, 40, f'Current Visibility \n           {visibility}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    cloudcover = current['cloudcover']
    ax.text(31, 40, f'Current Cloud Cover in % \n              {cloudcover}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    solarradiation = current['solarradiation']
    ax.text(75, 40, f'Current solar radiation \n              {solarradiation}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    solarenergy = current['solarenergy']
    ax.text(-10, 15, f'Current solar energy \n              {solarenergy}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    uvindex = current['uvindex']
    ax.text(75, 15, f'Current UV Index \n  {uvindex}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    sunrise = (datetime.datetime.fromtimestamp(current['sunriseEpoch']).strftime('%H:%M:%S'))
    ax.text(-10, -5, f'Today Sun Rais Time : {sunrise}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    sunset = (datetime.datetime.fromtimestamp(current['sunsetEpoch']).strftime('%H:%M:%S'))
    ax.text(65, -5, f'Today Set Rais Time : {sunset}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    ax.set(xlim=(0, 100), ylim=(0, 100))
    plt.grid(False)
    plt.axis('off')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    ##  hours data

    hours = data['days'][0]['hours']

    time = [hours[i]['datetime'] for i in range(24)]

    temp = [hours[i]['temp'] for i in range(24)]
    fig,ax =plt.subplots(figsize=(10,6))
    # ax.text(0.5, 0.5, 'SAAMS', transform=ax.transAxes,fontsize=150, color='gray', alpha=0.5,ha='center', va='center', rotation=30)
    plt.title("24 Hours Temperature Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(time,temp,marker='*',color='r')
    plt.legend([f'Minimum {round(min(temp),2)}\nAverage {round(sum(temp)/len(temp),2)}\nMaximum {round(max(temp),2)}'])
    plt.grid(True)
    plt.ylabel("Temperature in °C")
    plt.subplots_adjust(bottom=0.15)
    for index in range(len(temp)):
        ax.text(time[index], temp[index], temp[index], size=8)
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)



    humidity = [hours[i]['humidity'] for i in range(24)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours Humidity Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(time,humidity,marker='o',color='b')
    plt.grid(True)
    plt.ylabel("Humidity in %")
    plt.legend([f'Minimum {round(min(humidity),2)}\nAverage {round(sum(humidity)/len(humidity),2)}\nMaximum {round(max(humidity),2)}'])
    plt.subplots_adjust(bottom=0.15)
    for index in range(len(humidity)):
        ax.text(time[index], humidity[index], humidity[index], size=8)
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    dew = [hours[i]['dew'] for i in range(24)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours Dew Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(time,dew,marker='^',color='#000055')
    plt.legend([f'Minimum {round(min(dew),2)}\nAverage {round(sum(dew)/len(dew),2)}\nMaximum {round(max(dew),2)}'])
    plt.grid(True)
    plt.ylabel("Dew")
    plt.subplots_adjust(bottom=0.15)
    for index in range(len(dew)):
        ax.text(time[index], dew[index], dew[index], size=8)
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)



    winddir = [hours[i]['winddir'] for i in range(24)]
    windspeed = [hours[i]['windspeed'] for i in range(24)]
    ax = WindroseAxes.from_ax(figsize=(12,8))
    WindroseAxes.set_title(ax,"Wind Direction And Speed(Km/h)")
    ax.bar(winddir,windspeed, normed=True, opening=0.3, edgecolor='white')
    ax.set_legend()
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    pressure = [hours[i]['pressure'] for i in range(24)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours Pressure Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(time,pressure,marker='+',color='#000055')
    plt.grid(True)
    plt.ylabel("Pressure")
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(pressure),2)}\nAverage {round(sum(pressure)/len(pressure),2)}\nMaximum {round(max(pressure),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    cloudcover = [hours[i]['cloudcover'] for i in range(24)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours Pressure Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.grid(True)
    plt.ylabel("Cloud Cover in %")
    plt.plot(time,cloudcover,marker='d',color='#000055')
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(cloudcover),2)}\nAverage {round(sum(cloudcover)/len(cloudcover),2)}\nMaximum {round(max(cloudcover),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    visibility = [hours[i]['visibility'] for i in range(24)]
    solarradiation = [hours[i]['solarradiation'] for i in range(24)]
    solarenergy  = [hours[i]['solarenergy'] for i in range(24)]
    uvindex = [hours[i]['uvindex'] for i in range(24)]
    severerisk = [hours[i]['severerisk'] for i in range(24)]
    for i in range(len(solarenergy)):
        if(solarenergy[i]==None):
            solarenergy[i] = 0

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)
    fig.suptitle("Today 24 hours Others Parameter",fontsize=16)

    ax.text(-10, 90, f'24 Hours   Minimum Visibility {min(visibility)}      Avarage Visibility {round(sum(visibility)/len(visibility))}     Maximum Visibility {min(visibility)}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')
    ax.text(-10, 70, f'24 Hours Minimum solarradiation {min(solarradiation)}   Avarage solarradiation {round(sum(solarradiation)/len(solarradiation))}  Maximum solarradiation {min(solarradiation)}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')
    ax.text(-10, 50, f'24 Hours Minimum solarenergy {min(solarenergy)}   Avarage solarenergy {round(sum(solarenergy)/len(solarenergy))}  Maximum solarenergy {min(solarenergy)}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')
    ax.text(-10, 30, f'24 Hours Minimum uvindex {min(uvindex)}   Avarage uvindex {round(sum(uvindex)/len(uvindex))}  Maximum uvindex {min(uvindex)}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')
    ax.text(-10, 10, f'24 Hours Minimum severerisk {min(severerisk)}   Avarage severerisk {round(sum(severerisk)/len(severerisk))}  Maximum severerisk {min(severerisk)}', style='italic',bbox={'facecolor': '#ff00ff','alpha': 0.5,'boxstyle':"round,pad=0.8"},fontsize=12,fontweight='bold')

    ax.set(xlim=(0, 100), ylim=(0, 100))
    plt.grid(False)
    plt.axis('off')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)



    #days


    day = data['days']

    dates = [day[i]['datetime'] for i in range(15)]

    tempmax = [day[i]['tempmax'] for i in range(15)]
    tempmin = [day[i]['tempmin'] for i in range(15)]
    temp = [day[i]['temp'] for i in range(15)]

    fig,ax =plt.subplots(figsize=(10,6))
    X_axis = np.arange(len(dates))
    plt.title("Next 15 Days Temprature",fontsize=16,pad=20)
    plt.bar(X_axis,tempmin,0.2,color='#552000')
    plt.bar(X_axis + 0.2,temp,0.2,color='#990000')
    plt.bar(X_axis + 0.4,tempmax,0.2,color='#ff0000')
    plt.legend(['minimun','avarage','maximum'])
    plt.xticks(rotation=90,fontsize=6)
    plt.xticks(X_axis, dates)
    plt.grid(True,linestyle = '--', linewidth = 0.5)
    plt.subplots_adjust(bottom=0.15)
    plt.ylabel("Temepature in C")
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    dew = [day[i]['dew'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("Next 15 Days Dew",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=6)
    plt.plot(dates,dew,marker='^',color='#000055',label="Minimun : \nAvarage: \nMaximun:")
    plt.grid(True)
    plt.ylabel("Dew")
    plt.subplots_adjust(bottom=0.15)
    for index in range(len(dew)):
        ax.text(dates[index], dew[index], dew[index], size=8)
    plt.legend([f'Minimum {round(min(dew),2)}\nAverage {round(sum(dew)/len(dew),2)}\nMaximum {round(max(dew),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    humidity = [day[i]['humidity'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("Next 15 Days Humidity",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=6)
    plt.plot(dates,humidity,marker='o',color='b')
    plt.grid(True)
    plt.ylabel("Humidity in %")
    plt.subplots_adjust(bottom=0.15)
    for index in range(len(humidity)):
        ax.text(dates[index], humidity[index], humidity[index], size=8)
    plt.legend([f'Minimum {round(min(humidity),2)}\nAverage {round(sum(humidity)/len(humidity),2)}\nMaximum {round(max(humidity),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    windspeed = [day[i]['windspeed'] for i in range(15)]
    winddir = [day[i]['winddir'] for i in range(15)]
    ax = WindroseAxes.from_ax(figsize=(12,8))
    WindroseAxes.set_title(ax,"Wind Direction And Speed(Km/h)")
    ax.bar(winddir,windspeed, normed=True, opening=0.3, edgecolor='white')
    ax.set_legend()
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    pressure = [day[i]['pressure'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours Pressure Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(dates,pressure,marker='+',color='#000055')
    plt.grid(True)
    plt.ylabel("Pressure in Pa")
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(pressure),2)}\nAverage {round(sum(pressure)/len(pressure),2)}\nMaximum {round(max(pressure),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)



    visibility = [day[i]['visibility'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours visibility Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(dates,visibility,marker='+',color='#000055')
    plt.grid(True)
    plt.ylabel("visibility")
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(visibility),2)}\nAverage {round(sum(visibility)/len(visibility),2)}\nMaximum {round(max(visibility),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)



    solarradiation = [day[i]['solarradiation'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours solarradiation Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(dates,solarradiation,marker='+',color='#000055')
    plt.grid(True)
    plt.ylabel("solarradiation")
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(solarradiation),2)}\nAverage {round(sum(solarradiation)/len(solarradiation),2)}\nMaximum {round(max(solarradiation),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)

    solarenergy = [day[i]['solarenergy'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours solarenergy Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(dates,solarenergy,marker='+',color='#000055')
    plt.grid(True)
    plt.ylabel("solarenergy")
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(solarenergy),2)}\nAverage {round(sum(solarenergy)/len(solarenergy),2)}\nMaximum {round(max(solarenergy),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    severerisk = [day[i]['severerisk'] for i in range(15)]
    fig,ax =plt.subplots(figsize=(10,6))
    plt.title("24 Hours severerisk Data",fontsize=16,pad=20)
    plt.xticks(rotation=90,fontsize=8)
    plt.plot(dates,severerisk,marker='+',color='#000055')
    plt.grid(True)
    plt.ylabel("severerisk")
    plt.subplots_adjust(bottom=0.15)
    plt.legend([f'Minimum {round(min(severerisk),2)}\nAverage {round(sum(severerisk)/len(severerisk),2)}\nMaximum {round(max(severerisk),2)}'])
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)



    cloudcover = [day[i]['cloudcover'] for i in range(15)]

    fig,ax =plt.subplots(figsize=(10,6))
    plt.suptitle("15 Days Cloud Cover Data",fontsize=16)
    plt.subplots_adjust(hspace=0.4,wspace=0.4)
    for i in range(1,7):
        plt.subplot(2,3,i)
        plt.pie([cloudcover[i-1],100-cloudcover[i-1]],colors=['#a8bbd9','#5bcdfa'],labels=['Cloud Cover','Open'],autopct='%1.1f%%',explode=[0.1,0.1],textprops={'fontsize': 8})
        plt.xlabel(dates[i-1],fontsize=8,fontweight='bold')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)

    fig,ax =plt.subplots(figsize=(10,6))
    plt.suptitle("15 Days Cloud Cover Data",fontsize=16)
    plt.subplots_adjust(hspace=0.4,wspace=0.4)
    for i in range(7,13):
        plt.subplot(2,3,i-6)
        plt.pie([cloudcover[i-1],100-cloudcover[i-1]],colors=['#a8bbd9','#5bcdfa'],labels=['Cloud Cover','Open'],autopct='%1.1f%%',explode=[0.1,0.1],textprops={'fontsize': 8})
        plt.xlabel(dates[i-1],fontsize=8,fontweight='bold')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)

    fig,ax =plt.subplots(figsize=(10,6))
    plt.suptitle("15 Days Cloud Cover Data",fontsize=16)
    plt.subplots_adjust(hspace=0.4,wspace=0.4)
    for i in range(13,16):
        plt.subplot(2,3,i-12)
        plt.pie([cloudcover[i-1],100-cloudcover[i-1]],colors=['#a8bbd9','#5bcdfa'],labels=['Cloud Cover','Open'],autopct='%1.1f%%',explode=[0.1,0.1],textprops={'fontsize': 8})
        plt.xlabel(dates[i-1],fontsize=8,fontweight='bold')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    ##date sun rais and sunset nu table batavi devanu
    sunrise = [day[i]['sunriseEpoch'] for i in range(15)]
    sunset = [day[i]['sunsetEpoch'] for i in range(15)]

    sundata = [[day[i]['datetime'],(datetime.datetime.fromtimestamp(day[i]['sunriseEpoch']).strftime('%H:%M:%S')),(datetime.datetime.fromtimestamp(day[i]['sunsetEpoch']).strftime('%H:%M:%S'))] for i in range(15)]
    sundata.insert(0,["DATE","SUN RAIS","SUN SET"])
    fig, ax = plt.subplots(figsize=(10,6))
    plt.title("next 15 days Sun set and sun rais data",fontsize=16,pad=20)
    table = ax.table(cellText=sundata, loc='center')
    table.set_fontsize(9)
    table.scale(1,1.8)
    ax.axis('off')
    # plt.show()
    fig.savefig(p, format='pdf')
    plt.close(fig)


    p.close()


    # def save_image(filename):
    #     p = PdfPages(filename)
    #     fig_nums = plt.get_fignums()
    #     figs = [plt.figure(n) for n in fig_nums]
    #     for fig in figs:
    #         fig.savefig(p, format='pdf')
    #     p.close()
    # filename = "multi_plot_image.pdf"

    # save_image(filename)




from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS settings
origins = ["*"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/get_report")
async def get_pdf(farmername: str, farmname: str, latitude: str, longitude: str):
    try:
        Create_PDF(farmername,farmname,latitude,longitude)
        file_path = "report.pdf"
        return FileResponse(file_path, media_type="application/pdf")
    except:
        return {"Error":"Something gets Wrong..."}