[num, text, raw] = xlsread('BusData.xlsx');
startTime = text(:,6);
endTime = text(:, 7);
newTable = cell(25536,2);
for i = 1:25536;
    newTable(i,1) = cellstr(datestr(startTime(i+2), 'HH:MM'));
    newTable(i,2) = cellstr(datestr(endTime(i+2), 'HH:MM'));
end
%xlswrite('newTable.xls', newtable);