class Solution:
    def getRow(self, rowIndex):
        row = [1]

        for i in range(1, rowIndex + 1):
            newRow = [1]
            for j in range(1, i):
                newRow.append(row[j - 1] + row[j])
            newRow.append(1)
            row = newRow

        return row