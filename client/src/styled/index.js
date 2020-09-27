import styled from '@emotion/styled'


export const Section = styled.div`
  background-color: black;
  border-radius: 10px;
  padding: 10px 20px;
  max-width: 300px;
  text-align: center;
`

export const Button = styled.button`
  color: black;
  background-color: white;
  border: none;
  padding: 10px 15px;
  margin: 5px;
  width: 75px;
  text-align: center;
  outline: unset;
  &:focus{
    color: red;
  }
  `
export const ViewCount = styled.p`
  color: white;
  font-size: 30px;
`

export const Title = styled.h5`
  color: white;
  font-size: 24px;

`

